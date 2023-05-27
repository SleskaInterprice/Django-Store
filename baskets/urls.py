from django.urls import path

from baskets.views import add_product, delete_basket

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>', add_product, name='add_product'),
    path('delete/<int:basket_id>', delete_basket, name='delete_basket'),
]
