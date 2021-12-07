from django.urls import path
from . import views

app_name = "main" # for namespacing of urls.

urlpatterns = [
  path("", views.homepage, name="homepage"),
]