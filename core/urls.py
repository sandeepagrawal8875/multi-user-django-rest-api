from django.urls import path

from .views import SellerRegistrationView, BuyerRegistrationView

app_name = 'core'

urlpatterns = [
    path('registration/seller/', SellerRegistrationView.as_view(), name = 'register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name = 'register-buyer'),
]