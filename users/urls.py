from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import IndexView, AuthorizationView, RegistrationView, profile, add_product, delete_basket

app_name = 'user'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', AuthorizationView.as_view(), name='authorization'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('basket/add/<int:product_id>', add_product, name='add_product'),
    path('basket/delete/<int:basket_id>', delete_basket, name='delete_basket'),
]
