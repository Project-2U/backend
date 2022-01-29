from django.contrib import admin

from .models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'state', 'total']
    list_filter = ['state', 'date']
    readonly_fields = ["date"]
