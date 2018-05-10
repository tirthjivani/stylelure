from django.shortcuts import render,redirect
from .models import Wishlist,WishlistItem
from Products.models import Product
# from billing.models import BillingProfile




def wishlist_home(request):
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
    # print(request.session.get('wishlist_id'))
 
    return render(request,'wishlist.html',{"wishlist": wishlist_obj})

def wishlist_add(request):
   # wishlist_obj, new_obj = wishlist.objects.new_or_get(request)
   # print(wishlist_obj)
    product_id = request.POST.get('product_id')
    selected_color = request.POST.get('selected_color')
    selected_size = request.POST.get('selected_size')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("wishlist:wishlist")
        wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
        #print('a',wishlist.items.all())
        
        try:
            qs = WishlistItem.objects.get(wishlist=wishlist_obj,
                product=product_id,selected_color=selected_color,
                selected_size=selected_size)
            qs.quantity += 1
            qs.save()

        except WishlistItem.DoesNotExist:
            WishlistItem.objects.create(product=product_obj,wishlist=wishlist_obj,
            selected_color=selected_color,selected_size=selected_size)
        wishlist_id = request.session.get('wishlist_id')
     
    return redirect("wishlist:wishlist")


def wishlist_update(request):
    product_id = request.POST.get('product_id')
    wishlist_item_id = request.POST.get('wishlist_item_id')
    wishlist_id = request.session.get('wishlist_id')
    quantity = request.POST.get('quantity')

             
    qs = WishlistItem.objects.get(id=wishlist_item_id)
    qs.quantity=quantity
    qs.save()
    
    return redirect('wishlist:wishlist')



def wishlist_remove(request):
    product_id = request.POST.get('product_id')
    wishlist_item_id = request.POST.get('wishlist_item_id')
    wishlist_id = request.session.get('wishlist_id')
    # print('as',wishlist_id)
    # print(product_id)
    # import pdb; pdb.set_trace()
    WishlistItem.objects.filter(id=wishlist_item_id).all().delete()   
    return redirect('wishlist:wishlist')
