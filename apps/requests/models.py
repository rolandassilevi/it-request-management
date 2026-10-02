from django.conf import settings
from django.db import models

from apps.catalog.models import Product
from apps.organizations.models import Contact, Organization


class Request(models.Model):

    class Status(models.TextChoices):
        NEW = "NEW", "Nouvelle"
        TO_ANALYZE = "TO_ANALYZE", "À analyser"
        IN_PROGRESS = "IN_PROGRESS", "En cours"
        OFFER_SENT = "OFFER_SENT", "Offre envoyée"
        WON = "WON", "Gagnée"
        LOST = "LOST", "Perdue"
        CLOSED = "CLOSED", "Clôturée"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="requests",
    )

    contact = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        related_name="requests",
    )

    reference = models.CharField(
        max_length=30,
        unique=True,
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    desired_date = models.DateField(
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_requests",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.reference} - {self.organization.name}"


class RequestItem(models.Model):

    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="request_items",
    )

    quantity = models.PositiveIntegerField()

    notes = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return f"{self.request.reference} - {self.product.name} x {self.quantity}"