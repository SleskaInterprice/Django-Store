from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, RedirectView

from users.forms import UserLoginForm, UserForm, UserEditForm
from users.models import Basket
from products.models import Product


class IndexView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return '/user/profile/' if self.request.user.is_authenticated else '/user/login/'


class AuthorizationView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = 'user/login'


@login_required
def profile(request):
    form = UserEditForm(instance=request.user)
    if request.method == 'POST':
        user = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        user.save()
        return HttpResponseRedirect(reverse('user:profile'))
    context = {
        'form': form,
        'basket_list': Basket.objects.filter(user_id=request.user.id),
    }
    return render(request, 'users/profile.html', context)


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

