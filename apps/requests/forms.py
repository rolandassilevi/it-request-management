from django import forms

from .models import Request, RequestItem


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            "organization",
            "contact",
            "reference",
            "title",
            "description",
            "status",
            "desired_date",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "desired_date": forms.DateInput(attrs={"type": "date"}),
        }


class RequestItemForm(forms.ModelForm):
    class Meta:
        model = RequestItem
        fields = [
            "product",
            "quantity",
            "notes",
        ]