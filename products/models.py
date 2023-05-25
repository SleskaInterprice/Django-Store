from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=6)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    image = models.ImageField(verbose_name='Изображение', upload_to='products_images')
    category = models.ForeignKey(verbose_name='Категория', to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
