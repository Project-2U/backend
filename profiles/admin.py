from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

# Register your models here.



admin.site.unregister(Group)
admin.site.site_header="Sitio de Administración para Autoelectricos del Cauca"

@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=UserProfile
    exclude = ("username",)
    list_display = (
        "user_email",
        "is_active",
        "user_type",
        "last_login"
    )
    list_filter = (
        "user_email",
        "is_active",
        'user_type'
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user_email",
                    "password",
                    "user_type",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "user_email",
                    "password1",
                    "password2",
                    "user_type",
                    "is_active"
                ),
            },
        ),
    )
    search_fields = ("user_email",)
    ordering = ("user_email",)
    list_editable=['is_active', 'user_type']


