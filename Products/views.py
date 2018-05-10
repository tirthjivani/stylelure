from django.shortcuts import render,get_object_or_404
from .models import Product,ProductImages,Category
from cart.models import Cart
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(active=True)
    page = request.GET.get('page', 1)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    paginator = Paginator(products_list, 3)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)
    context= {'category': category,'products_list':products_list,'categories': categories ,'topics':topics}
    return render(request,'products/product_list.html',context)


def product_list_view(request, category_slug=None):
    # import pdb; pdb.set_trace()
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(active=True)
    page = request.GET.get('page', 1)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    paginator = Paginator(products_list, 3)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)
    context= {'category': category,'products_list':products_list,'categories': categories ,'topics':topics}
    return render(request,'products/product_list_view.html',context)

def product_detail(request,id, slug):
    instance = Product.objects.get_by_id(id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    size = instance.available_size
    if instance is None:
        raise Http404("Product doesn't exist")

    context = {
        'cart_obj':cart_obj,
        'object': instance,
        'object_size': size
    }

    print(size)
    return render(request, "products/detail.html", context)
# Create your views here.


