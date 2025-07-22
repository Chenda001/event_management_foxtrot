from django.db import models
from django.contrib.auth.models import User

# Make sure Space model exists in venue app
from venue.models import Space  

class Booking(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Who booked
    purpose = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    approved = models.BooleanField(default=False)  # Admin approval
    created_at = models.DateTimeField(auto_now_add=True)

    