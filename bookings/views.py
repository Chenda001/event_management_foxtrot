from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def booking_list(request):
    """
    Show all bookings (optional: filter by user or show all for admin).
    Currently shows *all* bookings.
    """
    bookings = Booking.objects.select_related('venue', 'user').all()



    context = {
        'bookings': bookings,
    }
    return render(request, 'bookings/booking_list.html', context)