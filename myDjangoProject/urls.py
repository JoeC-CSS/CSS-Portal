from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("hosts/", include("vuln_man.urls")),
    path("admin/", admin.site.urls),
]
