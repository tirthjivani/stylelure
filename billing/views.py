from django.shortcuts import render
from .models import BillingProfile
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
from cart.models import Cart
from billing.models import BillingProfile
from orders.models import Order
from datetime import datetime


@csrf_exempt
def payment_done(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
    order_obj.updated=datetime.now()
    order_obj.save()
    # order_obj.status='paid'
    # order_obj.save()
    # cart_obj.delete()
    #import pdb; pdb.set_trace()
    context = {
            "object": order_obj,
            "billing_profile": billing_profile,
        }
    return render(request, 'payment/done.html',context)


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_process(request):
    pass

# Create your views here.
