from django.shortcuts import render

from Products.models import Product,Category
# Create your views here.

def search_product_list(request, category_slug=None):
    category = None
    search=None
    categories = Category.objects.all()
    #search = Product.objects.all().featured()
    products_list = Product.objects.filter(active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    context= {'category': category,'products_list':products_list,'categories': categories,"search":search }

    if request.method == 'GET':
        query = request.GET.get('q',None)
        if query is not None:
            search = Product.objects.search(query)
            return render(request,'search/search_product_list.html',{'category': category,
            'products_list':products_list,'categories': categories,"search":search})
        else:
            search = Product.objects.all().featured()
            return render(request,'search/search_product_list.html',context)
    return render(request,'search/search_product_list.html',context)
