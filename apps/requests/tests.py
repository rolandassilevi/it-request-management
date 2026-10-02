# from django.test import TestCase

from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.catalog.models import Category, Product
from apps.organizations.models import Contact, Organization

from .models import Request, RequestItem


class RequestModelTests(TestCase):

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        self.organization = Organization.objects.create(
            name="ONG Test",
            organization_type=Organization.OrganizationType.NGO,
            registration_number="TEST-001",
            city="Montréal",
            country="Canada",
        )

        self.contact = Contact.objects.create(
            organization=self.organization,
            first_name="Marie",
            last_name="Test",
            job_title="Responsable",
            email="marie@example.com",
            is_primary=True,
        )

        self.category = Category.objects.create(
            name="Ordinateurs",
            code="TEST-COMPUTERS",
        )

        self.product = Product.objects.create(
            category=self.category,
            name="Laptop Test",
            sku="TEST-LAPTOP-001",
            brand="Test",
            model="T100",
            unit_price=Decimal("999.99"),
        )

        self.request_obj = Request.objects.create(
            organization=self.organization,
            contact=self.contact,
            reference="REQ-TEST-001",
            title="Demande test",
            desired_date=date.today(),
            created_by=self.user,
        )


    def test_request_creation(self):
        self.assertEqual(
            self.request_obj.reference,
            "REQ-TEST-001",
        )


    def test_request_item_relationship(self):
        item = RequestItem.objects.create(
            request=self.request_obj,
            product=self.product,
            quantity=10,
        )

        self.assertEqual(
            self.request_obj.items.count(),
            1,
        )

        self.assertEqual(
            item.product,
            self.product,
        )


class RequestViewTests(TestCase):

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="webuser",
            password="TestPassword123!",
        )


    def test_request_list_requires_authentication(self):
        response = self.client.get(
            reverse("requests:request_list")
        )

        self.assertEqual(response.status_code, 302)


    def test_authenticated_user_can_view_requests(self):
        self.client.login(
            username="webuser",
            password="TestPassword123!",
        )

        response = self.client.get(
            reverse("requests:request_list")
        )

        self.assertEqual(response.status_code, 200)


    def test_authenticated_user_can_open_create_form(self):
        self.client.login(
            username="webuser",
            password="TestPassword123!",
        )

        response = self.client.get(
            reverse("requests:request_create")
        )

        self.assertEqual(response.status_code, 200)