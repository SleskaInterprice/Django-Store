from django.db import models

from products.models import Product
from users.models import User


class BasketManager(models.QuerySet):
    def total_sum(self):
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
