from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, RedirectView

from users.forms import UserLoginForm, UserForm, UserEditForm


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
    }
    return render(request, 'users/profile.html', context)
