from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "code", "description", "is_active"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "sku",
            "brand",
            "model",
            "description",
            "unit_price",
            "is_active",
        ]