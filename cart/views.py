from django.shortcuts import render,redirect
from .models import Cart,CartItem
from Products.models import Product
from billing.models import BillingProfile
from accounts.models import GuestEmail 
from accounts.forms import GuestForm
from addresses.models import Address
from orders.models import Order
from coupons.forms import CouponApplyForm

def wishlist(request):
    return render(request,'cart/wishlist.html')

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(request.session.get('cart_id'))
    # coupon_apply_form = CouponApplyForm()

    return render(request,'cart/cart.html',{"cart": cart_obj})

def cart_add(request):
   # cart_obj, new_obj = Cart.objects.new_or_get(request)
   # print(cart_obj)
    product_id = request.POST.get('product_id')
    selected_color = request.POST.get('selected_color')
    selected_size = request.POST.get('selected_size')
   # print(selected_color)
  # selected_color=rgb2hex(selected_color[0],selected_color[1],selected_color[2])
    #print(selected_size)
    # total=cart_obj.get_total_cost
    # print(total)
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:cart")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        #print('a',Cart.items.all())
        
        cart_id = request.session.get('cart_id')
        #print('a',item_list(id=cart_id))
        # print(product_id)
        # import pdb; pdb.set_trace()
        # if product_id in item_list(id=cart_id):            
        #     CartItem.objects.get(product_obj)
        # else:
        CartItem.objects.create(product=product_obj,cart=cart_obj,
            selected_color=selected_color,selected_size=selected_size)

        # return redirect(product_obj.get_absolute_url())
    return redirect("cart:cart")


def cart_update(request):
    product_id = request.POST.get('product_id')
    cart_item_id = request.POST.get('cart_item_id')
    cart_id = request.session.get('cart_id')
    if product_id in item_list(id=cart_id):            
        CartItem.objects.get(id=cart_item_id)
    else:
        pass





def cart_remove(request):
    product_id = request.POST.get('product_id')
    cart_item_id = request.POST.get('cart_item_id')
    cart_id = request.session.get('cart_id')
    # print('as',cart_id)
    # print(product_id)
    # import pdb; pdb.set_trace()
    if product_id in item_list(id=cart_id): 
        CartItem.objects.filter(id=cart_item_id).all().delete()   
    return redirect('cart:cart')

product_list=[]
def item_list(id):        
    item_count = Cart.objects.filter(id=id).first().items.all().count()
    for i in range(item_count):
        product_=str(Cart.objects.filter(id=id).first().items.all()[i].product_id)
        product_list.append(product_)
    return product_list


# def rgb2hex(r,g,b):
#     return "#{:02x}{:02x}{:02x}".format(r,g,b)

def checkout_home(request):
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
            return redirect("cart:cart")
        try:   
            order_obj.billing_address = Address.objects.get(billing_profile=billing_profile.id,address_type='billing') 
        except Address.DoesNotExist:
            print(" Address is gone?")
            return redirect("cart:cart")
        if order_obj.billing_address or order_obj.shipping_address:
            order_obj.save()
    

    # print(order_obj.billing_address)
    context = {
          'coupon_apply_form':coupon_apply_form,
        "object": order_obj,
        "billing_profile": billing_profile,
        "guest_form": guest_form,
        "address_qs": address_qs,
    }
    return render(request, "order_overview.html", context)