from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, OrganizationForm
from .models import Contact, Organization


@login_required
def organization_list(request):
    organizations = Organization.objects.prefetch_related("contacts").order_by("name")

    return render(
        request,
        "organizations/organization_list.html",
        {"organizations": organizations},
    )


@login_required
def organization_detail(request, pk):
    organization = get_object_or_404(
        Organization.objects.prefetch_related("contacts"),
        pk=pk,
    )

    return render(
        request,
        "organizations/organization_detail.html",
        {"organization": organization},
    )


@login_required
def organization_create(request):
    form = OrganizationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        organization = form.save()

        messages.success(
            request,
            "Organisation créée avec succès.",
        )

        return redirect(
            "organizations:organization_detail",
            pk=organization.pk,
        )

    return render(
        request,
        "organizations/organization_form.html",
        {
            "form": form,
            "page_title": "Nouvelle organisation",
        },
    )


@login_required
def organization_update(request, pk):
    organization = get_object_or_404(Organization, pk=pk)

    form = OrganizationForm(
        request.POST or None,
        instance=organization,
    )

    if request.method == "POST" and form.is_valid():
        organization = form.save()

        messages.success(
            request,
            "Organisation modifiée avec succès.",
        )

        return redirect(
            "organizations:organization_detail",
            pk=organization.pk,
        )

    return render(
        request,
        "organizations/organization_form.html",
        {
            "form": form,
            "organization": organization,
            "page_title": "Modifier l'organisation",
        },
    )


@login_required
def organization_toggle_active(request, pk):
    organization = get_object_or_404(Organization, pk=pk)

    if request.method == "POST":
        organization.is_active = not organization.is_active
        organization.save(update_fields=["is_active"])

        messages.success(
            request,
            "Statut de l'organisation mis à jour.",
        )

    return redirect(
        "organizations:organization_detail",
        pk=organization.pk,
    )


@login_required
def contact_list(request):
    contacts = Contact.objects.select_related("organization").order_by(
        "organization__name",
        "last_name",
        "first_name",
    )

    return render(
        request,
        "organizations/contact_list.html",
        {"contacts": contacts},
    )


@login_required
def contact_create(request):
    initial = {}

    organization_id = request.GET.get("organization")

    if organization_id:
        initial["organization"] = organization_id

    form = ContactForm(
        request.POST or None,
        initial=initial,
    )

    if request.method == "POST" and form.is_valid():
        contact = form.save()

        messages.success(
            request,
            "Contact créé avec succès.",
        )

        return redirect(
            "organizations:organization_detail",
            pk=contact.organization_id,
        )

    return render(
        request,
        "organizations/contact_form.html",
        {
            "form": form,
            "page_title": "Nouveau contact",
        },
    )


@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    form = ContactForm(
        request.POST or None,
        instance=contact,
    )

    if request.method == "POST" and form.is_valid():
        contact = form.save()

        messages.success(
            request,
            "Contact modifié avec succès.",
        )

        return redirect(
            "organizations:organization_detail",
            pk=contact.organization_id,
        )

    return render(
        request,
        "organizations/contact_form.html",
        {
            "form": form,
            "contact": contact,
            "page_title": "Modifier le contact",
        },
    )


@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    organization_id = contact.organization_id

    if request.method == "POST":
        contact.delete()

        messages.success(
            request,
            "Contact supprimé avec succès.",
        )

    return redirect(
        "organizations:organization_detail",
        pk=organization_id,
    )