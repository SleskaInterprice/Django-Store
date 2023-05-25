from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from products import urls as products_urls
from products.views import IndexView
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include(products_urls, namespace='products')),
    path('user/', include(users_urls, namespace='user')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
