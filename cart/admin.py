from django.contrib import admin
from .models import Cart,CartItem



class CartItemInline(admin.StackedInline):
    model = CartItem
    extra = 0
#admin.site.register(CartItem,CartItemInline)

class CartAdmin(admin.ModelAdmin):
    # list_display = ['id', 'user', 'subtotal', 'total', 'Cart.items', 'created_date', 'updated']

    inlines = [ CartItemInline]

admin.site.register(Cart,CartAdmin)


# Register your models here.
