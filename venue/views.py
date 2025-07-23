from django.shortcuts import render, get_object_or_404, redirect
from .models import Space

def space_list(request):
    spaces = Space.objects.all()
    return render(request, 'venue/space_list.html', {'spaces': spaces})

def book_space(request, space_id):
    """
    Books the space if not already booked, then redirects to space list.
    """
    space = get_object_or_404(Space, pk=space_id)
    if not space.is_booked:  # only allow booking if free
        space.is_booked = True
        space.save()
    return redirect('venue:space_list')
