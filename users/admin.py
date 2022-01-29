from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "lastname", "age", "phone", "address", "occupation", "user_profile", "create_at",
                    "update_at"]
    list_filter = ["name", "lastname", "age", "occupation"]
    readonly_fields = ["create_at", "update_at"]