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
            "issue_date": forms.DateInput(attrs={"type": "date"}),
            "valid_until": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4}),
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