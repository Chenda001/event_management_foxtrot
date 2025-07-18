from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Venue, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'event_date', 'approved')
    list_filter = ('approved', 'event_type', 'event_date')
    search_fields = ('name', 'venue__name')

admin.site.register(Venue)
