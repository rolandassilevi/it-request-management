from django import forms

from .models import Contact, Organization


class BootstrapModelForm(forms.ModelForm):
    """Base form adding Bootstrap classes automatically."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class OrganizationForm(BootstrapModelForm):
    class Meta:
        model = Organization

        fields = [
            "name",
            "organization_type",
            "registration_number",
            "address",
            "city",
            "country",
            "phone",
            "email",
            "website",
            "description",
            "is_active",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class ContactForm(BootstrapModelForm):
    class Meta:
        model = Contact

        fields = [
            "organization",
            "first_name",
            "last_name",
            "job_title",
            "email",
            "phone",
            "is_primary",
        ]