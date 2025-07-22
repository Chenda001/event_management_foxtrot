from django.shortcuts import render, get_object_or_404, redirect
from .models import Space

def space_list(request):
    """
    Displays a list of all available spaces.
    """
    spaces = Space.objects.all()
    context = {
        'spaces': spaces
    }
    return render(request, 'space_list.html', context)

def book_space(request, space_id):
    """
    Toggles the booking status of a specific space.
    This is a simplified booking mechanism for demonstration.
    """
    space = get_object_or_404(Space, pk=space_id)
    # Toggle the booking status
    space.is_booked = not space.is_booked
    space.save()
    # Redirect back to the space list page
    return redirect('space_list')