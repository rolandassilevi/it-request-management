from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RequestForm, RequestItemForm
from .models import Request, RequestItem

from django.db.models import Q

@login_required
def request_list(request):
    requests = (
        Request.objects
        .select_related("organization", "contact", "created_by")
        .all()
        .order_by("-created_at")
    )

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()

    if query:
        requests = requests.filter(
            Q(reference__icontains=query)
            | Q(title__icontains=query)
            | Q(organization__name__icontains=query)
            | Q(contact__first_name__icontains=query)
            | Q(contact__last_name__icontains=query)
        )

    if status:
        requests = requests.filter(status=status)

    context = {
        "requests": requests,
        "query": query,
        "selected_status": status,
        "status_choices": Request.Status.choices,
        "request_count": requests.count(),
    }

    return render(
        request,
        "requests/request_list.html",
        context,
    )


@login_required
def request_detail(request, pk):
    request_obj = get_object_or_404(
        Request.objects
        .select_related("organization", "contact", "created_by")
        .prefetch_related("items__product"),
        pk=pk,
    )

    return render(
        request,
        "requests/request_detail.html",
        {"request_obj": request_obj},
    )


@login_required
def request_create(request):
    if request.method == "POST":
        form = RequestForm(request.POST)

        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.created_by = request.user
            request_obj.save()

            return redirect("requests:request_detail", pk=request_obj.pk)
    else:
        form = RequestForm()

    return render(
        request,
        "requests/request_form.html",
        {
            "form": form,
            "page_title": "Nouvelle demande",
        },
    )


@login_required
def request_update(request, pk):
    request_obj = get_object_or_404(Request, pk=pk)

    if request.method == "POST":
        form = RequestForm(request.POST, instance=request_obj)

        if form.is_valid():
            form.save()
            return redirect("requests:request_detail", pk=request_obj.pk)
    else:
        form = RequestForm(instance=request_obj)

    return render(
        request,
        "requests/request_form.html",
        {
            "form": form,
            "page_title": "Modifier la demande",
            "request_obj": request_obj,
        },
    )


@login_required
def request_item_create(request, request_pk):
    request_obj = get_object_or_404(Request, pk=request_pk)

    if request.method == "POST":
        form = RequestItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.request = request_obj
            item.save()

            return redirect("requests:request_detail", pk=request_obj.pk)
    else:
        form = RequestItemForm()

    return render(
        request,
        "requests/request_item_form.html",
        {
            "form": form,
            "request_obj": request_obj,
        },
    )
    
@login_required
def request_item_update(request, pk):
    item = get_object_or_404(RequestItem, pk=pk)

    if request.method == "POST":
        form = RequestItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect(
                "requests:request_detail",
                pk=item.request_id,
            )
    else:
        form = RequestItemForm(instance=item)

    return render(
        request,
        "requests/request_item_form.html",
        {
            "form": form,
            "request_obj": item.request,
            "page_title": "Modifier le produit demandé",
        },
    )


@login_required
def request_item_delete(request, pk):
    item = get_object_or_404(RequestItem, pk=pk)
    request_pk = item.request_id

    if request.method == "POST":
        item.delete()
        return redirect(
            "requests:request_detail",
            pk=request_pk,
        )

    return render(
        request,
        "requests/request_item_confirm_delete.html",
        {
            "item": item,
        },
    )