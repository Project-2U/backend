from django.contrib import admin
from django.contrib.admin import site

from .forms import ProductModelForm, ProductImageModelForm
from .models import Product, ProductImage
from orders.models import OrderProduct


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    form = ProductModelForm
    list_filter = ['name', 'is_active']
    list_display = ['name', 'amount', 'price', 'discount', 'reference', 'is_active']
    list_editable = ['amount', 'discount', 'price', 'is_active']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    form = ProductImageModelForm
    list_display = ['product','path_image']

site.register(Product, ProductAdmin)
