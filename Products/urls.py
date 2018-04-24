from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='product_list'),
    url(r'^detail/', views.detail, name='detail'),
  
]
