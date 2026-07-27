from django.contrib import admin
from core.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('date', 'user', 'created_at')
    ordering = ('-date',)

    