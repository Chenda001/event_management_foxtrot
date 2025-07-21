from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Venue, Booking
from .forms import BookingForm

@login_required
def view_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('view_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/view_booking.html', {'form': form})


