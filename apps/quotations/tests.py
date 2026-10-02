from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.catalog.models import Category, Product
from apps.organizations.models import Organization, Contact
from apps.requests.models import Request, RequestItem

from .models import Quotation, QuotationItem


class QuotationTests(TestCase):

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.organization = Organization.objects.create(
            name="ONG Test",
            organization_type="ONG",
            city="Montréal",
            country="Canada",
        )

        self.contact = Contact.objects.create(
            organization=self.organization,
            first_name="Marie",
            last_name="Test",
            email="marie@example.com",
        )

        self.category = Category.objects.create(
            name="Ordinateurs",
            code="TEST-COMPUTERS",
            description="Test"
        )

        self.product = Product.objects.create(
            category=self.category,
            name="Laptop Test",
            sku="TEST-LAPTOP-001",
            brand="Test",
            model="Model 1",
            unit_price=Decimal("1000.00"),
        )

        self.request_obj = Request.objects.create(
            organization=self.organization,
            contact=self.contact,
            reference="REQ-TEST-001",
            title="Demande test",
            created_by=self.user,
        )

        RequestItem.objects.create(
            request=self.request_obj,
            product=self.product,
            quantity=2,
        )

        self.quotation = Quotation.objects.create(
            request=self.request_obj,
            reference="QUO-TEST-001",
            status=Quotation.Status.DRAFT,
            issue_date=date.today(),
            valid_until=date.today() + timedelta(days=30),
            created_by=self.user,
        )

        self.item = QuotationItem.objects.create(
            quotation=self.quotation,
            product=self.product,
            quantity=2,
            unit_price=Decimal("1000.00"),
        )

    def test_quotation_creation(self):
        self.assertEqual(
            self.quotation.reference,
            "QUO-TEST-001"
        )

    def test_quotation_request_relationship(self):
        self.assertEqual(
            self.quotation.request,
            self.request_obj
        )

    def test_line_total(self):
        self.assertEqual(
            self.item.line_total,
            Decimal("2000.00")
        )

    def test_quotation_subtotal(self):
        self.assertEqual(
            self.quotation.subtotal,
            Decimal("2000.00")
        )

    def test_quotation_list_requires_authentication(self):
        response = self.client.get(
            reverse("quotations:quotation_list")
        )

        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_view_quotation(self):
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.get(
            reverse(
                "quotations:quotation_detail",
                args=[self.quotation.pk],
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "QUO-TEST-001")
        
    def test_sent_quotation_updates_request_status(self):
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.post(
            reverse(
                "quotations:quotation_update",
                args=[self.quotation.pk],
            ),
            {
                "reference": self.quotation.reference,
                "status": Quotation.Status.SENT,
                "issue_date": self.quotation.issue_date,
                "valid_until": self.quotation.valid_until,
                "notes": "",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.request_obj.refresh_from_db()

        self.assertEqual(
            self.request_obj.status,
            "OFFER_SENT",
        )


    def test_accepted_quotation_updates_request_status(self):
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        self.client.post(
            reverse(
                "quotations:quotation_update",
                args=[self.quotation.pk],
            ),
            {
                "reference": self.quotation.reference,
                "status": Quotation.Status.ACCEPTED,
                "issue_date": self.quotation.issue_date,
                "valid_until": self.quotation.valid_until,
                "notes": "",
            },
        )

        self.request_obj.refresh_from_db()

        self.assertEqual(
            self.request_obj.status,
            "WON",
    )