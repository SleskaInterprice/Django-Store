from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import reverse

from products.models import Product


class User(AbstractUser):
    image = models.ImageField(verbose_name='Изображение', upload_to='user_images', null=True, blank=True)
    is_verified_email = models.BooleanField(verbose_name='Верифицированный', default=False)


class BasketManager(models.QuerySet):
    def total_summ(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name='Прдукт', to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)

    objects = BasketManager.as_manager()

    def sum(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Корзина пользователя: {self.user} | товар: {self.product.name}'


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.TimeField(auto_now_add=True)
    expiration = models.TimeField()

    def __str__(self):
        return f'Email verification for {self.user.username}'

    def send_mail_verification(self):
        mail = f'для подтверждения почты перейдите по ссылке \b {settings.BASE_URL}' \
               f'{reverse("user:email_verification",kwargs={"code": self.code})}'
        send_mail('Тема', mail, settings.EMAIL_HOST_USER, [self.user.email])
