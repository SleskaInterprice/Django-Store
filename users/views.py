from datetime import datetime

from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.views.generic import CreateView, RedirectView, TemplateView
from django.views.generic.edit import UpdateView

from common.view import TitleMixin
from users.forms import UserEditForm, UserForm, UserLoginForm
from users.models import EmailVerification, User


class IndexView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('user:profile', kwargs={'pk': self.request.user.id})
        return reverse('user:authorization')


class AuthorizationView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    title = 'Store | Авторизация'


class RegistrationView(TitleMixin, CreateView):
    template_name = 'users/register.html'
    form_class = UserForm

    title = 'Store | Регистрация'

    def get_success_url(self):
        return reverse('user:authorization')


class ProfileView(TitleMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserEditForm
    model = User

    title = 'Store | Профиль'

    def get_success_url(self):
        return reverse('user:profile', kwargs={'pk': self.request.user.id})


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'

    title = 'Store | Подтверждение почты'

    def get(self, request, *args, **kwargs):
        res = super(EmailVerificationView, self).get(self.request)
        verification_elem = EmailVerification.objects.filter(code=self.kwargs.get('code'))
        if verification_elem.exists():
            verification_elem = verification_elem.first()
            user = verification_elem.user
            if verification_elem.expiration < datetime.now().time():
                user.is_verified_email = True
                user.save()
                verification_elem.delete()
        return res

    def get_context_data(self, **kwargs):
        context = super(EmailVerificationView, self).get_context_data()
        context['success'] = True
        verification_elem = EmailVerification.objects.filter(code=self.kwargs.get('code'))
        if not verification_elem or verification_elem.expiration > datetime.now().time():
            context['success'] = False
        return context
