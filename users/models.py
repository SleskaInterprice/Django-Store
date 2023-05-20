from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product


class User(AbstractUser):
    image = models.ImageField(verbose_name='Изображение', upload_to='user_images', null=True, blank=True)


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
