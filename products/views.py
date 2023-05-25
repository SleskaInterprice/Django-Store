from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.view import TitleMixin
from products.models import Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'

    title = 'Store'


class ProductsView(TitleMixin, ListView):
    template_name = 'products/products.html'
    paginate_by = 3
    model = Product

    title = 'Store - Каталог'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['category_id'] = self.kwargs.get('category_id', 0)
        return context

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        if self.kwargs.get('category'):
            queryset = queryset.filter(category=self.kwargs['category'])
        return queryset
