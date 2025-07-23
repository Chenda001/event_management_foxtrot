from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'event_date', 'approved')
    list_filter = ('approved', 'event_type', 'event_date')
    search_fields = ('name', 'venue__name')
