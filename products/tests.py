from django.test import TestCase
from django.shortcuts import reverse
from http import HTTPStatus

from products.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    fixtures = ['products/fixtures/products.json', 'products/fixtures/products-category.json']

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')
        self.assertEqual(response.context_data['title'], 'Store')

    def test_products(self):
        path = reverse('products:products')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['categories']), list(ProductCategory.objects.all()))
        self.assertEqual(list(response.context_data['page_obj']), list(Product.objects.all())[:3])

