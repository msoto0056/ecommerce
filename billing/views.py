from django.conf import settings
from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

from .models import BillingProfile, Card

import stripe

STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY", "sk_test_51IRg1WJaIbGmBAOdAh0FxwTnhS7XLoTkHIFuYjejlHekiKBhmo2T9VOqeNE92uSs57nvYes798jhew9NX2L7TPu400Yz61ht4v")
STRIPE_PUB_KEY =  getattr(settings, "STRIPE_PUB_KEY", 'pk_test_51IRg1WJaIbGmBAOdsizxW00zGGS4MLJSUiNd4C1vj5hV4Sswp3JF4zFUdVSw6xZBPxn3990On1EIzRQnWGuEEQBh00mqsgm5UK')
stripe.api_key = STRIPE_SECRET_KEY

def payment_method_view(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})

def payment_method_createview(request):
    #if request.method == "POST" and request.is_ajax():
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": "Success! Your card was added."})
    return HttpResponse("error", status_code=401)