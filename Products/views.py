from django.shortcuts import render,get_object_or_404
from .models import Product,ProductImages,Category
from django.http import Http404


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    context= {'category': category,'products_list':products_list,'categories': categories }
    return render(request,'products/product_list.html',context)


def product_detail(request,id, slug):
    instance = Product.objects.get_by_id(id)
    size = instance.available_size
    if instance is None:
        raise Http404("Product doesn't exist")

    context = {
        'object': instance,
        'obejct_size': size
    }
    return render(request, "products/detail.html", context)
# Create your views here.


