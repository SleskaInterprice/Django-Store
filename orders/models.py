from django.db import models
from users.models import User


class Orders(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3

    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    email = models.CharField(verbose_name='Email', max_length=256)
    address = models.CharField(verbose_name='Адрес', max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)

    def __str__(self):
        return f'Заказ №{self.id}. {self.first_name} {self.last_name}'
