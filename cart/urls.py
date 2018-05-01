from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart_home, name='cart'),
    url(r'^update/$', views.cart_update, name='update'),
    url(r'^add/$', views.cart_add, name='add'),
    url(r'^cart/$', views.cart_remove, name='delate'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),

]
