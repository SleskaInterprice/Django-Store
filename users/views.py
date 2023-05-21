from django.shortcuts import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, RedirectView
from django.views.generic.edit import UpdateView

from users.forms import UserLoginForm, UserForm, UserEditForm
from users.models import Basket, User
from products.models import Product


class IndexView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('user:profile', kwargs={'pk': self.request.user.id})
        return reverse('user:authorization')


class AuthorizationView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user:authorization')


class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = UserEditForm
    model = User

    def get_success_url(self):
        return reverse('user:profile', kwargs={'pk': self.request.user.id})

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['basket_list'] = Basket.objects.filter(user_id=self.request.user.id)
        return context


def add_product(request, product_id=None, quantity=1):
    product = Product.objects.get(id=product_id)
    user_basket = Basket.objects.filter(user=request.user, product=product)
    if not user_basket.exists():
        basket = Basket(user=request.user, quantity=1, product=product)
        basket.save()
    else:
        user_basket = user_basket.first()
        user_basket.quantity += quantity
        user_basket.save()
    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])


def delete_basket(request, basket_id):
    basket = Basket.objects.filter(id=basket_id)
    if basket.exists():
        basket.first().delete()
    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])

