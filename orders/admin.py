from django.contrib import admin

from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['user','ord_state', 'ord_total']
    list_filter=['ord_state',]