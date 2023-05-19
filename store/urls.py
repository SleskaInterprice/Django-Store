from django.contrib import admin
from django.urls import path, include
from products.views import IndexView
from products import urls as products_urls
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include(products_urls, namespace='products')),
    path('user/', include(users_urls, namespace='user')),
]
