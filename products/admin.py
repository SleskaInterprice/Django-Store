from django.contrib import admin

from products.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    search_fields = ('name', 'description')
    ordering = ('name', 'price')


admin.site.register(ProductCategory)
