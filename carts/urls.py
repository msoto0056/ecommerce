from django.urls import path,re_path, reverse

from .views import (
        cart_home, 
        cart_update, 
        )

app_name = 'carts'
urlpatterns = [
    path('cart/', cart_home, name='home'),
    path('cart/update/', cart_update, name='update'),
]

