from django.contrib import admin
from .models import User
from .forms import UserModelForm


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserModelForm
    list_display = ["name", "lastname", "age", "phone", "address", "occupation", "user_profile", "create_at",
                    "update_at"]
    list_filter = ["name", "lastname", "age", "occupation"]
    readonly_fields = ["create_at", "update_at"]
