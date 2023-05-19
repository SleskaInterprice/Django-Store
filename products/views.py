from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView

from products.models import ProductCategory, Product


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context



def products(request, category=None, number_of_page=1):
    categories = ProductCategory.objects.all()
    products_list = Product.objects.all()

    if category:
        products_list = products_list.filter(category_id=category)

    paginator = Paginator(products_list, 3)
    products_list = paginator.page(number_of_page)

    context = {
        'title': 'Store - Каталог',
        'products_list': products_list,
        'categories': categories,
        'number_of_page': 1,
        'paginator': paginator,
        'category_id': category or 0,
    }
    return render(request, template_name='products/products.html', context=context)
