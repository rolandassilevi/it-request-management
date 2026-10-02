from django.urls import path

from . import views


app_name = "organizations"


urlpatterns = [
    path(
        "",
        views.organization_list,
        name="organization_list",
    ),
    path(
        "new/",
        views.organization_create,
        name="organization_create",
    ),
    path(
        "<int:pk>/",
        views.organization_detail,
        name="organization_detail",
    ),
    path(
        "<int:pk>/edit/",
        views.organization_update,
        name="organization_update",
    ),
    path(
        "<int:pk>/toggle-active/",
        views.organization_toggle_active,
        name="organization_toggle_active",
    ),

    path(
        "contacts/",
        views.contact_list,
        name="contact_list",
    ),
    path(
        "contacts/new/",
        views.contact_create,
        name="contact_create",
    ),
    path(
        "contacts/<int:pk>/edit/",
        views.contact_update,
        name="contact_update",
    ),
    path(
        "contacts/<int:pk>/delete/",
        views.contact_delete,
        name="contact_delete",
    ),
]