from django.db import models

class Organization(models.Model):

    class OrganizationType(models.TextChoices):
        SME = "SME", "PME"
        NGO = "NGO", "ONG"
        INSTITUTION = "INSTITUTION", "Institution"
        SCHOOL = "SCHOOL", "École"
        COMPANY = "COMPANY", "Entreprise"
        ASSOCIATION = "ASSOCIATION", "Association"
        MINISTRY = "MINISTRY", "Ministère"
        BANK = "BANK", "Banque"
        HOSPITAL = "HOSPITAL", "Hôpital"
        OTHER = "OTHER", "Autre"

    name = models.CharField(max_length=150)

    organization_type = models.CharField(
        max_length=20,
        choices=OrganizationType.choices,
    )

    registration_number = models.CharField(
        max_length=100,
        blank=True,
    )

    address = models.CharField(
        max_length=255,
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Contact(models.Model):

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="contacts",
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )

    job_title = models.CharField(
        max_length=150,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
