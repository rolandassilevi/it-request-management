from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.catalog.models import Category, Product
from apps.organizations.models import Contact, Organization
from apps.requests.models import Request
from apps.quotations.models import Quotation


@login_required
def dashboard(request):
    
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
    
    context = {
        "organization_count": Organization.objects.count(),
        "contact_count": Contact.objects.count(),
        "category_count": Category.objects.count(),
        "product_count": Product.objects.count(),
        "request_count": Request.objects.count(),
        "new_request_count": Request.objects.filter(
            status=Request.Status.NEW
        ).count(),
        "in_progress_request_count": Request.objects.filter(
            status=Request.Status.IN_PROGRESS
        ).count(),
        
        "quotation_count": quotation_count,
        "quotation_draft_count": quotation_draft_count,
        "quotation_sent_count": quotation_sent_count,
        "quotation_accepted_count": quotation_accepted_count,
        
    }

    return render(request, "dashboard.html", context)