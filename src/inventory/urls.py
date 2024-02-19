from django.urls import path
from .views import CheckOutView

urlpatterns = [
    path("check_out/", CheckOutView.as_view(), name="check_out"),
]
