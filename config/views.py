from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.catalog.models import Category, Product
from apps.organizations.models import Contact, Organization
from apps.requests.models import Request
from apps.quotations.models import Quotation


@login_required
def dashboard(request):

    # ---------------------------------------------------------
    # Organisations / catalogue
    # ---------------------------------------------------------

    organization_count = Organization.objects.count()
    contact_count = Contact.objects.count()
    category_count = Category.objects.count()
    product_count = Product.objects.count()

    # ---------------------------------------------------------
    # Demandes
    # ---------------------------------------------------------

    request_count = Request.objects.count()

    new_request_count = Request.objects.filter(
        status=Request.Status.NEW
    ).count()

    to_analyze_request_count = Request.objects.filter(
        status=Request.Status.TO_ANALYZE
    ).count()

    in_progress_request_count = Request.objects.filter(
        status=Request.Status.IN_PROGRESS
    ).count()

    offer_sent_request_count = Request.objects.filter(
        status=Request.Status.OFFER_SENT
    ).count()

    won_request_count = Request.objects.filter(
        status=Request.Status.WON
    ).count()

    lost_request_count = Request.objects.filter(
        status=Request.Status.LOST
    ).count()

    closed_request_count = Request.objects.filter(
        status=Request.Status.CLOSED
    ).count()

    # ---------------------------------------------------------
    # Cotations
    # ---------------------------------------------------------

    quotation_count = Quotation.objects.count()

    quotation_draft_count = Quotation.objects.filter(
        status=Quotation.Status.DRAFT
    ).count()

    quotation_sent_count = Quotation.objects.filter(
        status=Quotation.Status.SENT
    ).count()

    quotation_accepted_count = Quotation.objects.filter(
        status=Quotation.Status.ACCEPTED
    ).count()

    quotation_rejected_count = Quotation.objects.filter(
        status=Quotation.Status.REJECTED
    ).count()

    quotation_expired_count = Quotation.objects.filter(
        status=Quotation.Status.EXPIRED
    ).count()

    # Cotations encore commercialement actives
    active_quotation_count = Quotation.objects.filter(
        status__in=[
            Quotation.Status.DRAFT,
            Quotation.Status.SENT,
        ]
    ).count()


    # ---------------------------------------------------------
    # Contexte du dashboard
    # ---------------------------------------------------------

    context = {
        "organization_count": organization_count,
        "contact_count": contact_count,
        "category_count": category_count,
        "product_count": product_count,

        "request_count": request_count,
        "new_request_count": new_request_count,
        "to_analyze_request_count": to_analyze_request_count,
        "in_progress_request_count": in_progress_request_count,
        "offer_sent_request_count": offer_sent_request_count,
        "won_request_count": won_request_count,
        "lost_request_count": lost_request_count,
        "closed_request_count": closed_request_count,

        "quotation_count": quotation_count,
        "quotation_draft_count": quotation_draft_count,
        "quotation_sent_count": quotation_sent_count,
        "quotation_accepted_count": quotation_accepted_count,
        "quotation_rejected_count": quotation_rejected_count,
        "quotation_expired_count": quotation_expired_count,
        "active_quotation_count": active_quotation_count,
    }

    return render(request, "dashboard.html", context)