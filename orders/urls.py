from django.urls import path
from .views import OrderHistoryView
from .views import *

urlpatterns = [
    path("history/", OrderHistoryView.as_view(), name="order-history"),
]
