from django.shortcuts import render
from bookings.models import Booking
from venue.models import Space  # Needed for venue filter
from django.utils import timezone

def event_list(request):
    now = timezone.now()
    bookings = Booking.objects.filter(approved=True)

    # GET filters
    space_id = request.GET.get('space')
    start = request.GET.get('start_date')
    end = request.GET.get('end_date')

    # Apply filters
    if space_id:
        bookings = bookings.filter(space__id=space_id)
    if start:
        bookings = bookings.filter(start_datetime__date__gte=start)
    if end:
        bookings = bookings.filter(end_datetime__date__lte=end)

    # Categorize
    ongoing = bookings.filter(start_datetime__lte=now, end_datetime__gte=now)
    upcoming = bookings.filter(start_datetime__gt=now)
    past = bookings.filter(end_datetime__lt=now)

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
