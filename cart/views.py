from django.shortcuts import render

def wishlist(request):
    return render(request,'cart/wishlist.html')

def cart(request):
    return render(request,'cart/cart.html')
# Create your views here.
