from django.urls import path
from core.views import PostView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", PostView.as_view(), name="test-view"),
    path("api/token", obtain_auth_token, name="auth-token"),
]
