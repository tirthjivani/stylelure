from django.db import models
from django.conf import settings
from Products.models import Product
# from django.db.models.signals import pre_save, post_save, m2m_changed,post_delete
from colorfield.fields import ColorField
from datetime import datetime

User = settings.AUTH_USER_MODEL


class WishlistManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        if request.user.id == None:
            user=None
        qs = Wishlist.objects.filter(user=user)
    
        if qs.count() > 0:
            new_obj = False
            wishlist_obj = qs.first()
            print(wishlist_obj)
            request.session['wishlist_id'] = wishlist_obj.id

            if request.user.is_authenticated() and wishlist_obj.user is None:
                wishlist_obj.user = request.user
                wishlist_obj.save()
       
        else:
            Wishlist_obj = Wishlist.objects.new(user=request.user)
            new_obj = True
            request.session['wishlist_id'] = wishlist_obj.id
        return wishlist_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Wishlist(models.Model):
    user           = models.ForeignKey(User, null=True, blank=True)
    #products      = models.ManyToManyField(Product, blank=True)
    updated        = models.DateTimeField(auto_now=True)
    created_date   = models.DateTimeField(auto_now_add=True)
    count          = models.PositiveIntegerField(default=0)

    objects = WishlistManager()

    def __str__(self):
        return str(self.id)

class WishlistItem(models.Model):
    product = models.ForeignKey(Product,related_name='wishlist_products',on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist,related_name='wishlist_items',null=True,on_delete=models.CASCADE)
    selected_color = ColorField(default=None)
    quantity = models.PositiveIntegerField(default=1)
    selected_size  = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.discounted_price * self.quantity