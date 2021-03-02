from django.urls import path,re_path, reverse
from django.contrib.auth.views import LogoutView

from .views import RegisterView, LoginView, guest_register_view 


app_name = 'accounts'
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('register/guest/',guest_register_view,name='guest'),
]


