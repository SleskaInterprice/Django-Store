from django.urls import path

from products.views import ProductsView

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('category/<int:category>/page/<int:page>/', ProductsView.as_view(), name='filtered_products'),
]
