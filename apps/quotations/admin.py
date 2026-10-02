from django.contrib import admin

from .models import Quotation, QuotationItem


class QuotationItemInline(admin.TabularInline):
    model = QuotationItem
    extra = 1


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "request",
        "status",
        "issue_date",
        "valid_until",
        "created_by",
    )
    list_filter = ("status", "issue_date", "valid_until")
    search_fields = (
        "reference",
        "request__reference",
        "request__organization__name",
    )
    inlines = [QuotationItemInline]


@admin.register(QuotationItem)
class QuotationItemAdmin(admin.ModelAdmin):
    list_display = (
        "quotation",
        "product",
        "quantity",
        "unit_price",
        "line_total_display",
    )

    def line_total_display(self, obj):
        return obj.line_total

    line_total_display.short_description = "Total"