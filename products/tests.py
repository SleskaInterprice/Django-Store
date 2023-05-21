from django.test import TestCase
from django.shortcuts import reverse
from http import HTTPStatus


class IndexTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertTemplateUsed(response, 'products/index.html')
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertEqual(response.status_code, HTTPStatus.OK)
