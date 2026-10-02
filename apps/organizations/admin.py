from django.contrib import admin

from .models import Contact, Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization_type",
        "city",
        "country",
        "email",
        "is_active",
    )
    list_filter = ("organization_type", "country", "is_active")
    search_fields = ("name", "registration_number", "email", "city", "country")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "organization",
        "job_title",
        "email",
        "is_primary",
        "is_active",
    )
    list_filter = ("is_primary", "is_active")
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "organization__name",
    )