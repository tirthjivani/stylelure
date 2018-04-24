from django.contrib import admin
from .models import Product,Category

from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    # filter_horizontal = ('questions',)
    # fieldsets = (
    #     (None, {
    #         'fields': (('name', 'letter'), 'questions', 'color')
    #         }),
    #     )

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
# Register your models here.
