from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active", "created_at")
    search_fields = ("code", "name")
    list_filter = ("is_active",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "brand",
        "unit_price",
        "is_active",
    )
    search_fields = ("sku", "name", "brand", "model")
    list_filter = ("category", "is_active", "brand")
    ordering = ("name",)