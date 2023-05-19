from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import IndexView, AuthorizationView, RegistrationView, profile

app_name = 'user'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', AuthorizationView.as_view(), name='authorization'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
