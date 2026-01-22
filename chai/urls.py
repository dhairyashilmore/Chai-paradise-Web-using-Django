from django.urls import include, path
from . import views

urlpatterns = [
      path("", views.all_chai_items, name="all_chai_items"),
]