from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = Booking
        fields = [
            'name',
            'event_type',
            'expected_attendance',
            'poster',
            'description',
            'event_date',
            'venue'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)