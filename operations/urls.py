from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("delete/<int:id>/", views.Delete.as_view(), name="delete"),
    path("display/<int:id>/", views.Display.as_view(), name="display"),
    path("update/<int:id>", views.Update.as_view(), name="update"),
]
