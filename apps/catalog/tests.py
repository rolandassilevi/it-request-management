# from django.test import TestCase
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class CatalogModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Ordinateurs",
            code="COMPUTERS",
        )

        self.product = Product.objects.create(
            category=self.category,
            name="Test Laptop",
            sku="TEST-001",
            unit_price=Decimal("999.99"),
        )

    def test_category_product_relationship(self):
        self.assertEqual(self.category.products.count(), 1)

    def test_product_price(self):
        self.assertEqual(self.product.unit_price, Decimal("999.99"))

    def test_category_is_protected(self):
        with self.assertRaises(ProtectedError):
            self.category.delete()


class CatalogViewTests(TestCase):

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="catalogtester",
            password="TestPassword123!",
        )

        self.category = Category.objects.create(
            name="Réseau",
            code="NETWORK",
        )

    def test_catalog_requires_authentication(self):
        response = self.client.get(reverse("catalog:product_list"))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_view_catalog(self):
        self.client.login(
            username="catalogtester",
            password="TestPassword123!",
        )

        response = self.client.get(reverse("catalog:product_list"))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_create_product(self):
        self.client.login(
            username="catalogtester",
            password="TestPassword123!",
        )

        response = self.client.post(
            reverse("catalog:product_create"),
            {
                "category": self.category.pk,
                "name": "Router Test",
                "sku": "ROUTER-001",
                "brand": "TP-Link",
                "model": "Test",
                "description": "",
                "unit_price": "99.99",
                "is_active": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(sku="ROUTER-001").exists())
