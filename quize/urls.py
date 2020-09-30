from django.urls import path
from quize.views import QuizeView

urlpatterns = [path("", QuizeView.as_view(), name="quize-api-view")]
