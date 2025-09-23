from django.urls import path
from .views import *
from .views import EmailCheckView

urlpatterns = [
    path("check-email/", EmailCheckView.as_view(), name="check-email"),
]