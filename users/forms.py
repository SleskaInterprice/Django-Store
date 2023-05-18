from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}), label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password')


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), label='Имя пользователя')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), label='Фамилия')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}), label='Почта')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}), label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
