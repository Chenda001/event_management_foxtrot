from django.db import models
# create your
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    EVENT_TYPES = [
        ('academic', 'Academic'),
        ('religious', 'Religious'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    expected_attendance = models.PositiveIntegerField()
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    event_date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.venue.name}"
