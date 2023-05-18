from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout

from users.models import User
from users.forms import UserLoginForm, UserForm


def index(request):
    if not request.user:
        return HttpResponseRedirect(redirect_to=reverse('user:authorization'))
    return HttpResponseRedirect(redirect_to=reverse('user:profile'))


def authorization(request):
    if request.method == 'GET':
        context = {
            'form': UserLoginForm,
        }
        return render(request, 'users/login.html', context=context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(redirect_to=reverse('user:profile'))
            return HttpResponseNotFound()


def registration(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return HttpResponseRedirect(redirect_to=reverse('user:authorization'))
    if request.method == 'GET' or form.errors:
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)


def profile(request):
    return render(request, 'users/profile.html')


def use_logout(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse('index'))
