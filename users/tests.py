from http import HTTPStatus

from django.test import TestCase
from django.shortcuts import reverse

from users.models import User, Basket, EmailVerification
from users.forms import UserForm


class UserTestCase(TestCase):
    fixtures = ['products/fixtures/products.json', 'products/fixtures/products-category.json']

    def test_index(self):
        path = reverse('user:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('user:authorization'))

    def test_login(self):
        path = reverse('user:authorization')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_registration(self):
        path = reverse('user:registration')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

        # Не заполнена форма
        response = self.client.post(path, {})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertFalse(User.objects.all().exists())

        data = {
            'username': 'username', 'first_name': 'new_user_name',
            'last_name': 'new_user_name', 'email': 'email@email.com',
            'password1': 'pass12101!AA3', 'password2': '',
        }

        def failed_case(resp):
            self.assertEqual(resp.status_code, HTTPStatus.OK)
            self.assertFalse(User.objects.filter(username=data.get('username')).exists())

        self.assertFalse(User.objects.filter(username=data.get('username')).exists())

        # Не заполнен пароль
        response = self.client.post(path, data)
        failed_case(response)

        data['password2'] = data['password1']

        # Не заполнена почта
        data['email'] = ''
        response = self.client.post(path, data)
        failed_case(response)

        # Неверный формат почты
        data['email'] = 'email@email'
        response = self.client.post(path, data)
        failed_case(response)

        data['email'] = 'email@email.com'

        # Пароли не совпадают
        data['password1'] = 'email@email.com'
        response = self.client.post(path, data)
        failed_case(response)

        data['password1'] = data['password2']

        # Незаполнено 'Имя пользователя'
        data['username'] = ''
        response = self.client.post(path, data)
        failed_case(response)

        data['username'] = 'username'

        # Пароль похож на имя пользователя
        data['password1'] = 'username123'
        data['password2'] = data['password1']
        response = self.client.post(path, data)
        failed_case(response)

        # Пароль простой
        data['password1'] = '123'
        data['password2'] = data['password1']
        response = self.client.post(path, data)
        failed_case(response)

        data['password1'] = 'pass12101!AA3'
        data['password2'] = data['password1']

        # Заполнены все поля и всё валидно
        response = self.client.post(path, data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        users_query_set = User.objects.filter(username=data.get('username'))
        self.assertTrue(users_query_set.exists())

    def test_login(self):
        user = {
            'username': 'username', 'first_name': 'new_user_name',
            'last_name': 'new_user_name', 'email': 'email@email.com',
            'password1': 'pass12101!AA3', 'password2': 'pass12101!AA3',
        }
        self.client.post(reverse('user:registration'), user)
        response = self.client.post(
            reverse('user:authorization'), {'username': user['username'], 'password': user['password1']})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        self.assertFalse(Basket.objects.filter(user_id=response.user.id).exists())
