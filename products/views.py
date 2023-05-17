from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    return render(request, template_name='products/index.html')


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products_list': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, template_name='products/products.html', context=context)
