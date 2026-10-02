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

        labels = {
            "organization": "Structure",
            "contact": "Contact",
            "reference": "Référence",
            "title": "Objet",
            "description": "Description",
            "status": "Statut",
            "desired_date": "Date souhaitée",
        }

        widgets = {
            "organization": forms.Select(
                attrs={"class": "form-select"}
            ),

            "contact": forms.Select(
                attrs={"class": "form-select"}
            ),

            "reference": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. REQ-2026-002",
                }
            ),

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Renouvellement du parc informatique",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Décrivez le besoin en matériel...",
                }
            ),

            "status": forms.Select(
                attrs={"class": "form-select"}
            ),

            "desired_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }


class RequestItemForm(forms.ModelForm):
    class Meta:
        model = RequestItem

        fields = [
            "product",
            "quantity",
            "notes",
        ]

        widgets = {
            "product": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "placeholder": "Ex. 10",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Informations complémentaires sur le produit demandé",
                }
            ),
        }