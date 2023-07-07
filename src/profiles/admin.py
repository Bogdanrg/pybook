from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet, Technology
from django.utils.translation import gettext_lazy as _


class UserNetAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", 'middle_name', "last_name", "gender")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Additional info"), {"fields": ("phone", "avatar", "email")}),
    )
    list_display = ("id", "username", "email", "first_name", 'phone', "last_name", "is_staff")


admin.site.register(UserNet, UserNetAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )


admin.site.register(Technology, TechnologyAdmin)
