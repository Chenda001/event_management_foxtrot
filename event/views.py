from django.shortcuts import render
from bookings.models import Booking
from venue.models import Space
from django.utils import timezone

def event_list(request):
    now = timezone.now().date()  # only the date part
    bookings = Booking.objects.filter(approved=True)

    # GET filters
    space_id = request.GET.get('space')
    start = request.GET.get('start_date')
    end = request.GET.get('end_date')

    # Apply filters
    if space_id:
        bookings = bookings.filter(venue__id=space_id)
    if start:
        bookings = bookings.filter(event_date__gte=start)
    if end:
        bookings = bookings.filter(event_date__lte=end)

    # Categorize
    ongoing = bookings.filter(event_date=now)
    upcoming = bookings.filter(event_date__gt=now)
    past = bookings.filter(event_date__lt=now)

    context = {
        'ongoing_events': ongoing,
        'upcoming_events': upcoming,
        'past_events': past,
        'spaces': Space.objects.all(),  # For dropdown
        'selected_space': space_id,
        'start': start,
        'end': end,
    }
    return render(request, 'event/event_list.html', context)
