from django.urls import path

from users.views import index, authorization, registration, profile, use_logout

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('login/', authorization, name='authorization'),
    path('register/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', use_logout, name='logout')
]
