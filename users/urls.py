from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (AuthorizationView, EmailVerificationView, IndexView,
                         ProfileView, RegistrationView)

app_name = 'user'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', AuthorizationView.as_view(), name='authorization'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('profile/<pk>', login_required(ProfileView.as_view()), name='profile'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('email/verification/<code>', EmailVerificationView.as_view(), name='email_verification')
]
