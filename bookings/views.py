from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import  Booking
from .forms import BookingForm


@login_required
def booking_list(request):
    """
    Show all bookings (optional: filter by user or show all for admin).
    Currently shows *all* bookings.
    """
    bookings = Booking.objects.select_related('venue', 'user').all()

    # Optional: if you only want to show current user's bookings:
    # bookings = Booking.objects.filter(user=request.user).select_related('venue')

    context = {
        'bookings': bookings,
    }
    return render(request, 'bookings/booking_list.html', context)


