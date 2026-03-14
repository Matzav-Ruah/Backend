from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "streak_count",
        "is_staff",
        "is_superuser",
        "created_at",
        "updated_at",
        "events_last_updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "events_last_updated_at",
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("streak_count", "settings")}),
    )
