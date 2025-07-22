# spaces/admin.py

from django.contrib import admin
from .models import Space

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location', 'is_booked')
    list_filter = ('is_booked', 'capacity')
    search_fields = ('name', 'location')