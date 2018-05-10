from django.contrib import admin
from .models import Wishlist,WishlistItem



class WishlistItemInline(admin.StackedInline):
    model = WishlistItem
    extra = 0
#admin.site.register(WishlistItem,WishlistItemInline)

class WishlistAdmin(admin.ModelAdmin):
    # list_display = ['id', 'user', 'subtotal', 'total', 'Wishlist.items', 'created_date', 'updated']

    inlines = [ WishlistItemInline]

admin.site.register(Wishlist,WishlistAdmin)
