from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    return render(request, template_name='products/index.html')


def products(request, category=None):
    categories = ProductCategory.objects.all()
    products_list = Product.objects.all()
    print(category)

    if category:
        products_list = products_list.filter(category_id=category)

    context = {
        'title': 'Store - Каталог',
        'products_list': products_list,
        'categories': categories,
    }
    return render(request, template_name='products/products.html', context=context)
