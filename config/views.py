from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.catalog.models import Category, Product
from apps.organizations.models import Contact, Organization
from apps.requests.models import Request


@login_required
def dashboard(request):
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
    }

    return render(request, "dashboard.html", context)