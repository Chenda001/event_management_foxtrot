from django.shortcuts import render
from .models import Booking

def view_bookings(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})
