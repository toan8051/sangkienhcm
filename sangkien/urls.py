from django.urls import path
from .views import DonvivttpListView, SangkienListView, SangkienUpdate, SangkienCreate, SangkienDelete
#from .views import DepartmentView, IdeaListView, IdeaUpdate # new

urlpatterns = [
    path("", DonvivttpListView.as_view(), name="donvivttplist"), # new
    path("list/<int:list_id>/", SangkienListView.as_view(), name="sangkienlist"),

    # CRUD patterns for SangkienItems
    path(
        "list/<int:list_id>/sangkien/add/",
        SangkienCreate.as_view(),
        name="sangkien-add",
    ),

    path(
        "list/<int:list_id>/sangkien/<int:pk>/",
        SangkienUpdate.as_view(),
        name="sangkien-update",
    ),

    path(
        "list/<int:list_id>/sangkien/<int:pk>/delete/",
        SangkienDelete.as_view(),
        name="sangkien-delete",
    ),
]