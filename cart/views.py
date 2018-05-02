from django.shortcuts import render,redirect
from .models import Cart,CartItem
from Products.models import Product 

def wishlist(request):
    return render(request,'cart/wishlist.html')

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(request.session.get('cart_id'))
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
        CartItem.objects.filter(id=cart_item_id).delete()    
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