from django.shortcuts import render,redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm
from billing.models import BillingProfile
from orders.models import Order
from cart.models import Cart

@require_POST
def coupon_apply(request):
    now = timezone.now()
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    form = CouponApplyForm(request.POST)
    order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                    valid_from__lte=now,
                                    valid_to__gte=now,
                                    active=True)           
            print(coupon.id)
            order_obj.coupon=coupon
            order_obj.save()
        except Coupon.DoesNotExist:
            order_obj.coupon=None
            order_obj.save()
            request.session['coupon_id'] = None
    return redirect('overview')
