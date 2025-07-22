from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('space', 'user', 'start_datetime', 'end_datetime', 'approved')
    list_filter = ('approved', 'start_datetime')
    search_fields = ('space__name', 'user__username')
