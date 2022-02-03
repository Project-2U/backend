from django.contrib import admin

from .forms import NotificationModelForm
from .models import Notification


# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    form = NotificationModelForm
    list_display = ["title", "body", "date", "user", "order"]
    list_filter = ["date", "user", "order"]
    readonly_fields = ['date']
