from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("emotional_state", "user", "created_at", "updated_at")
    list_filter = ("emotional_state", "created_at", "updated_at")
    ordering = ("-updated_at",)
