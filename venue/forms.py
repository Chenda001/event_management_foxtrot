from django import forms
from .models import Venue, VenueReview, VenueCategory


class VenueSearchForm(forms.Form):
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search venues...',
            'class': 'form-control'
        })
    )
    category = forms.ModelChoiceField(
        queryset=VenueCategory.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    venue_type = forms.ChoiceField(
        choices=[('', 'All Types')] + Venue.VENUE_TYPES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    min_capacity = forms.IntegerField(
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Min capacity',
            'class': 'form-control'
        })
    )
    max_capacity = forms.IntegerField(
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Max capacity',
            'class': 'form-control'
        })
    )
    min_price = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Max price/hour',
            'class': 'form-control'
        })
    )
    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'City',
            'class': 'form-control'
        })
    )


class VenueReviewForm(forms.ModelForm):
    class Meta:
        model = VenueReview
        fields = ['rating', 'title', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review title'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review...'
            })
        }
