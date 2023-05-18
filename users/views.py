from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout

from users.forms import UserLoginForm, UserForm, UserEditForm


def index(request):
    if not request.user:
        return HttpResponseRedirect(redirect_to=reverse('user:authorization'))
    return HttpResponseRedirect(redirect_to=reverse('user:profile'))


def authorization(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(redirect_to=reverse('user:profile'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse('user:authorization'))
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def profile(request):
    form = UserEditForm(instance=request.user)
    if request.method == 'POST':
        user = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        print(user.errors)
        user.save()
        return HttpResponseRedirect(reverse('user:profile'))
    context = {
        'form': form,
    }
    return render(request, 'users/profile.html', context)


def use_logout(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse('index'))
