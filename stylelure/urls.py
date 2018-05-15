"""stylelure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from shop import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from addresses.views import checkout_address_create_view,address_update
from orders.views import overview
# from cart.views import checkout_home
from coupons.views import coupon_apply


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^account/',include('accounts.urls',namespace='accounts')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^contact/$', views.emailView, name='contact'),
    url(r'^address/$', address_update, name='address'),
    url(r'^address/add$', checkout_address_create_view, name='add_address'),
    url(r'^order/',include('orders.urls',namespace='order')),
    #url(r'^order/overview$', checkout_home, name='overview'),
    url(r'^apply/$',coupon_apply, name='apply'),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/',include('billing.urls',namespace='payment')),
    url(r'^contact/success$', views.successView, name='success'),
    url(r'^product/',include('Products.urls',namespace='Products')),
    url(r'^search/',include('search.urls',namespace='search')),
    # url(r'^review/', include('review.urls')),
    url(r'^cart/',include('cart.urls',namespace='cart')),
    url(r'^wishlist/',include('wishlist.urls',namespace='wishlist')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
