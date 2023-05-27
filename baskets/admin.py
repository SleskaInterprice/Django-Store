from django.contrib import admin
from baskets.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    fields = ('user', 'product', 'quantity')
