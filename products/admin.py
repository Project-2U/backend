from django.contrib import admin
from django.contrib.admin import site

from .forms import ProductModelForm
from .models import Product
from orders.models import OrderProduct


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    form = ProductModelForm
    list_filter = ['name', 'is_active']
    list_display = ['name', 'amount', 'price', 'discount', 'reference','is_active']
    list_editable = ['amount', 'discount', 'price', 'is_active']


site.register(Product, ProductAdmin)


