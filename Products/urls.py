from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^product_list/', views.product_list_view, name='product_list_view'),
    url(r'^product_list/(?P<category_slug>[-\w]+)/$', views.product_list_view, name='product_list_view_by_category'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
    
]
