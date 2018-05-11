from django.shortcuts import render,redirect
from coupons.forms import CouponApplyForm
from billing.models import BillingProfile
from accounts.models import GuestEmail 
from accounts.forms import GuestForm
from addresses.models import Address
from cart.models import Cart
from .models import Order

def overview(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.items.count() == 0:
        return redirect("cart:cart")  
    
    guest_form = GuestForm()
    coupon_apply_form = CouponApplyForm()

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    print(billing_profile)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated():
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)  
        try:
            order_obj.shipping_address = Address.objects.get(billing_profile=billing_profile.id,address_type='shipping')
        except Address.DoesNotExist:
            print("Show message to user, Address is gone?")
            # return redirect("address")
        try:   
            order_obj.billing_address = Address.objects.get(billing_profile=billing_profile.id,address_type='billing') 
        except Address.DoesNotExist:
            print(" Address is gone?")
            # return redirect("address")
        if order_obj.billing_address == None or order_obj.shipping_address == None:
            return redirect("address")

        if order_obj.billing_address or order_obj.shipping_address:
            order_obj.save()
    

    # print(order_obj.billing_address)
    context = {
        'form':coupon_apply_form,
        "object": order_obj,
        "billing_profile": billing_profile,
        "guest_form": guest_form,
        "address_qs": address_qs,
    }
    return render(request, "order_overview.html", context)


