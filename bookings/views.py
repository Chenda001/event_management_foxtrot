from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Venue, Booking
from .forms import BookingForm

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('venue_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})

def venue_list(request):
    venues = Venue.objects.all()
    booked_ids = Booking.objects.filter(approved=True).values_list('venue_id', flat=True)
    return render(request, 'bookings/venue_list.html', {
        'venues': venues,
        'booked_ids': booked_ids
    })

from django.shortcuts import render

def home (request):
    return render(request, 'bookings/home.html')