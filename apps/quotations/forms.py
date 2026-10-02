from django import forms

from .models import Quotation, QuotationItem


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [
            "reference",
            "status",
            "issue_date",
            "valid_until",
            "notes",
        ]

        widgets = {
            "reference": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. QUO-2026-001",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "issue_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "valid_until": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Informations complémentaires sur la cotation",
                }
            ),
        }


class QuotationItemForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = [
            "product",
            "quantity",
            "unit_price",
            "notes",
        ]

        widgets = {
            "product": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "Ex. 10",
                }
            ),
            "unit_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "step": "0.01",
                    "placeholder": "0.00",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Informations complémentaires sur ce produit",
                }
            ),
        }