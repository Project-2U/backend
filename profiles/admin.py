from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from admin_interface.models import Theme

# Register your models here.


admin.site.unregister(Group)
admin.site.unregister(Theme)


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserProfile
    exclude = ("name",)
    list_display = (
        "email",
        "is_active",
        "type",
        "last_login"
    )
    list_filter = (
        "email",
        "is_active",
        'type'
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "type",
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
                    "email",
                    "password1",
                    "password2",
                    "type",
                    "is_active"
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    list_editable = ['is_active', 'type']
