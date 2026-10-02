from django.urls import path

from . import views


app_name = "requests"

urlpatterns = [
    path("", views.request_list, name="request_list"),
    path("new/", views.request_create, name="request_create"),
    path("<int:pk>/", views.request_detail, name="request_detail"),
    path("<int:pk>/edit/", views.request_update, name="request_update"),
    path(
        "<int:request_pk>/items/new/",
        views.request_item_create,
        name="request_item_create",
    ),
    path(
        "items/<int:pk>/edit/",
        views.request_item_update,
        name="request_item_update",
    ),
    path(
        "items/<int:pk>/delete/",
        views.request_item_delete,
        name="request_item_delete",
    )
]