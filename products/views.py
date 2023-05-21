from django.shortcuts import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from products.models import ProductCategory, Product


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


class ProductsView(ListView):
    template_name = 'products/products.html'
    paginate_by = 3
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['title'] = 'Store - Каталог'
        context['category_id'] = self.kwargs.get('category_id', 0)
        return context

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        if self.kwargs.get('category'):
            queryset = queryset.filter(category=self.kwargs['category'])
        return queryset
