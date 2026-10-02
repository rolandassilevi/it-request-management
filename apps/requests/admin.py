from django.contrib import admin

from .models import Request, RequestItem


class RequestItemInline(admin.TabularInline):
    model = RequestItem
    extra = 1


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "organization",
        "contact",
        "title",
        "status",
        "desired_date",
        "created_at",
    )

    list_filter = (
        "status",
        "organization",
    )

    search_fields = (
        "reference",
        "title",
        "organization__name",
        "contact__first_name",
        "contact__last_name",
    )

    inlines = [RequestItemInline]


@admin.register(RequestItem)
class RequestItemAdmin(admin.ModelAdmin):
    list_display = (
        "request",
        "product",
        "quantity",
    )

    search_fields = (
        "request__reference",
        "product__name",
        "product__sku",
    )