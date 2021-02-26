from django.urls import path,re_path, reverse

from .views import (
        checkout_address_create_view,
        checkout_address_reuse_view,
        )

app_name = 'addresses'
urlpatterns = [
    path('checkout/address/create/', checkout_address_create_view, name='checkout_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_reuse'),
]

