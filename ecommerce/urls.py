"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

from billing.views import payment_method_view, payment_method_createview

from marketing.views import MarketingPreferenceUpdateView,MailchimpWebhookView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name='home'),
    path('about/',views.about_page,name='about'),
    path('contact/',views.contact_page,name='contact'),
    path('billing/payment-method/',payment_method_view,name='billing-payment-method'),
    path('billing/payment-method/create/',payment_method_createview,name='billing-payment-method-endpoint'),
    path('settings/email/',MarketingPreferenceUpdateView.as_view(),name='marketing-pref'),
    path('webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),
    path('', include('products.urls', namespace='products')),
    path('', include('search.urls', namespace='search')),
    path('', include('carts.urls', namespace='carts')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('addresses.urls', namespace='addresses')),
    
    #path('', include('orders.urls', namespace='order')),
    #path('<path/>'TemplateView.as_view(template_name='bootstrap/example.html')), 
    #path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    #path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)