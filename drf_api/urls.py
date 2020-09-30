from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("quize/", include("quize.urls")),
    path("core/", include("core.urls")),
    path("qs/", include("quickstart.urls")),
]