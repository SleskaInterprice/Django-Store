from django.urls import path
from products.views import products, ProductsView

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('page/<int:page>/', ProductsView.as_view(), name='test'),
    path('category/<int:category>/page/<int:page>/', ProductsView.as_view(), name='filtered_products'),
]
