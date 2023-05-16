from django.contrib import admin
from django.urls import path, include
from products.views import index
from products import urls as products_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products', include(products_url))
]
