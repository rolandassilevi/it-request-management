from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.requests.models import Request

from .forms import QuotationForm, QuotationItemForm
from .models import Quotation, QuotationItem

from django.contrib import messages

@login_required
def quotation_list(request):
    quotations = (
        Quotation.objects
        .select_related(
            "request",
            "request__organization",
            "created_by",
        )
        .prefetch_related("items")
    )

    return render(
        request,
        "quotations/quotation_list.html",
        {"quotations": quotations},
    )


@login_required
def quotation_detail(request, pk):
    quotation = get_object_or_404(
        Quotation.objects
        .select_related(
            "request",
            "request__organization",
            "request__contact",
            "created_by",
        )
        .prefetch_related("items__product"),
        pk=pk,
    )

    return render(
        request,
        "quotations/quotation_detail.html",
        {"quotation": quotation},
    )


@login_required
def quotation_create_from_request(request, request_pk):
    request_obj = get_object_or_404(Request, pk=request_pk)
    
    existing_quotation = Quotation.objects.filter(
        request=request_obj
    ).first()

    if existing_quotation:
        messages.info(
            request,
            f"La demande {request_obj.reference} possède déjà une cotation."
        )
        return redirect(
            "quotations:quotation_detail",
            pk=existing_quotation.pk,
        )

    if request.method == "POST":
        form = QuotationForm(request.POST)

        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.request = request_obj
            quotation.created_by = request.user
            quotation.save()

            for request_item in request_obj.items.select_related("product"):
                QuotationItem.objects.create(
                    quotation=quotation,
                    product=request_item.product,
                    quantity=request_item.quantity,
                    unit_price=request_item.product.unit_price,
                )

            return redirect(
                "quotations:quotation_detail",
                pk=quotation.pk,
            )
    else:
        form = QuotationForm(
            initial={
                "reference": f"QUO-{date.today().year}-",
                "status": Quotation.Status.DRAFT,
                "issue_date": date.today(),
                "valid_until": date.today() + timedelta(days=30),
            }
        )

    return render(
        request,
        "quotations/quotation_form.html",
        {
            "form": form,
            "request_obj": request_obj,
            "title": "Créer une cotation",
        },
    )


@login_required
def quotation_update(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)

    if request.method == "POST":
        form = QuotationForm(request.POST, instance=quotation)

        if form.is_valid():
            quotation = form.save()

            if quotation.status == Quotation.Status.SENT:
                quotation.request.status = "OFFER_SENT"

            elif quotation.status == Quotation.Status.ACCEPTED:
                quotation.request.status = "WON"

            elif quotation.status == Quotation.Status.REJECTED:
                quotation.request.status = "LOST"

            quotation.request.save()

            messages.success(
                request,
                f"La cotation {quotation.reference} a été mise à jour."
            )

            return redirect(
                "quotations:quotation_detail",
                pk=quotation.pk,
            )
    else:
        form = QuotationForm(instance=quotation)

    return render(
        request,
        "quotations/quotation_form.html",
        {
            "form": form,
            "request_obj": quotation.request,
            "quotation": quotation,
            "title": "Modifier la cotation",
        },
    )


@login_required
def quotation_item_create(request, quotation_pk):
    quotation = get_object_or_404(Quotation, pk=quotation_pk)

    if request.method == "POST":
        form = QuotationItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.quotation = quotation
            item.save()

            return redirect(
                "quotations:quotation_detail",
                pk=quotation.pk,
            )
    else:
        form = QuotationItemForm()

    return render(
        request,
        "quotations/quotation_item_form.html",
        {
            "form": form,
            "quotation": quotation,
            "title": "Ajouter un produit",
        },
    )


@login_required
def quotation_item_update(request, pk):
    item = get_object_or_404(QuotationItem, pk=pk)

    if request.method == "POST":
        form = QuotationItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect(
                "quotations:quotation_detail",
                pk=item.quotation.pk,
            )
    else:
        form = QuotationItemForm(instance=item)

    return render(
        request,
        "quotations/quotation_item_form.html",
        {
            "form": form,
            "quotation": item.quotation,
            "title": "Modifier le produit",
        },
    )


@login_required
def quotation_item_delete(request, pk):
    item = get_object_or_404(QuotationItem, pk=pk)
    quotation_pk = item.quotation.pk

    if request.method == "POST":
        item.delete()
        return redirect(
            "quotations:quotation_detail",
            pk=quotation_pk,
        )

    return render(
        request,
        "quotations/quotation_item_confirm_delete.html",
        {"item": item},
    )