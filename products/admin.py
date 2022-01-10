from django.contrib import admin
from .models import Product, OrderProduct

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter=['prod_name', 'is_active']
    list_display=['prod_name','prod_amount', 'prod_price', 'prod_discount', 'is_active']
    list_editable=['prod_amount', 'prod_discount', 'prod_price', 'is_active']

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display=['prod_id', 'order_id', 'quantity']
