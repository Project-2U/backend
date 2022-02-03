from django.contrib import admin

from .forms import CategoryModelForm
from .models import Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryModelForm
    list_display = ["name", "description", "create_at", "update_at"]
    list_filter = ["name", "create_at", "update_at"]
