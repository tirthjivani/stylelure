from django.shortcuts import render
from .models import Product,ProductImages
from django.http import Http404


def product_list(request):
	list_1=Product.objects.all()
	
	context={'list_1':list_1 }

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
