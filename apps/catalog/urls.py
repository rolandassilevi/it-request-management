from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_update, name="product_update"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/new/", views.category_create, name="category_create"),
    path(
        "categories/<int:pk>/edit/",
        views.category_update,
        name="category_update",
    ),
]