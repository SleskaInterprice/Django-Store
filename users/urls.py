from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import AuthorizationView, RegistrationView, add_product, delete_basket, ProfileView, IndexView, EmailVerificationView

app_name = 'user'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', AuthorizationView.as_view(), name='authorization'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('profile/<pk>', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('basket/add/<int:product_id>', add_product, name='add_product'),
    path('basket/delete/<int:basket_id>', delete_basket, name='delete_basket'),
    path('email/verification/<code>', EmailVerificationView.as_view(), name='email_verification')
]