from django.contrib import admin
from .models import Product,Category,ProductImages,ProductColors

from .forms import ProductForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_name', 'slug']
    prepopulated_fields = {'slug': ('Category_name',)}
admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.StackedInline):
    model = ProductImages
    extra = 1

class ProductColorsInline(admin.StackedInline):
    model = ProductColors
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    # list_display = ['title', 'slug', 'category', 'price', 'stock', 'active', 'created', 'updated']
    list_filter = ['active', 'created', 'updated', 'category']
    # list_editable = ['price', 'stock', 'active']
    prepopulated_fields = {'slug': ('title',)}

    inlines = [ ProductImageInline, ProductColorsInline]


    form = ProductForm
    # filter_horizontal = ('questions',)
    # fieldsets = (
    #     (None, {
    #         'fields': (('name', 'letter'), 'questions', 'color')
    #         }),
    #     )

admin.site.register(Product,ProductAdmin)
# admin.site.register(Category)
# Register your models here.
