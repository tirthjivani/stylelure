from django.shortcuts import render
from .models import Product,ProductImages

def index(request):
	list_1=Product.objects.all()
	
	context={'list_1':list_1 }

	return render(request,'products/product_list.html',context)


def detail(request):
	list_1=Product.objects.filter(id=2)
	context={'list_1':list_1}

	return render(request,'products/detail.html',context)
# Create your views here.
