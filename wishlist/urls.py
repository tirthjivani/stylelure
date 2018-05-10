from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.wishlist_home, name='wishlist'),
    url(r'^update/$', views.wishlist_update, name='update'),
    url(r'^add/$', views.wishlist_add, name='add'),
    url(r'^wishlist/$', views.wishlist_remove, name='delate'),
 
]
