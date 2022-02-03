from django.contrib import admin

from .forms import OrderProductModelForm
from .models import Order, OrderProduct


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'state', 'total']
    list_filter = ['state', 'date']
    readonly_fields = ["date"]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    form = OrderProductModelForm
    list_display = ['prod_id', 'order_id', 'quantity']
