from django.urls import path

from . import views


app_name = "quotations"

urlpatterns = [
    path("", views.quotation_list, name="quotation_list"),

    path(
        "request/<int:request_pk>/new/",
        views.quotation_create_from_request,
        name="quotation_create_from_request",
    ),

    path(
        "<int:pk>/",
        views.quotation_detail,
        name="quotation_detail",
    ),

    path(
        "<int:pk>/edit/",
        views.quotation_update,
        name="quotation_update",
    ),

    path(
        "<int:quotation_pk>/items/new/",
        views.quotation_item_create,
        name="quotation_item_create",
    ),

    path(
        "items/<int:pk>/edit/",
        views.quotation_item_update,
        name="quotation_item_update",
    ),

    path(
        "items/<int:pk>/delete/",
        views.quotation_item_delete,
        name="quotation_item_delete",
    ),
]