from django import forms

from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "code", "description", "is_active"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Ordinateurs",
                }
            ),
            "code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. COMPUTERS",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Description de la catégorie",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


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

        widgets = {
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Lenovo ThinkPad E14",
                }
            ),
            "sku": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. LNV-E14-001",
                }
            ),
            "brand": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Lenovo",
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. ThinkPad E14",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Description du produit",
                }
            ),
            "unit_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "0.00",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }