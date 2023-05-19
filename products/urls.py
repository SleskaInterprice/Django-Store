from django.urls import path
from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:category>/page/<number_of_page>/', products, name='filtered_products'),
]
