from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.search_product_list, name='query'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
]
