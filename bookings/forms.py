from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'event_type', 'expected_attendance', 'poster', 'description', 'event_date', 'venue']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
        }

