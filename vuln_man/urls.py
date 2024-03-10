from django.urls import path
from . import views

urlpatterns = [
    path("", views.HostView.as_view(), name="hosts"),
    path("vulnerabilities/", views.AllVulnerabilities.as_view(), name="vulnerabilities")

]