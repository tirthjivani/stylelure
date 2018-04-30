from django.shortcuts import render,redirect
from .models import Cart
from Products.models import Product 

def wishlist(request):
    return render(request,'cart/wishlist.html')

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(request.session.get('cart_id'))
    return render(request,'cart/cart.html',{"cart": cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    selected_color = request.POST.get('selected_color')
    selected_size = request.POST.get('selected_size')
    print(selected_color)
  # selected_color=rgb2hex(selected_color[0],selected_color[1],selected_color[2])
    print(selected_size)
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:cart")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        
        # return redirect(product_obj.get_absolute_url())
    return redirect("cart:cart")

# def rgb2hex(r,g,b):
#     return "#{:02x}{:02x}{:02x}".format(r,g,b)