from django.db import models

class Space(models.Model):
    """
    Represents a bookable space in the event management system.
    """
    name = models.CharField(max_length=200, help_text="Name of the space (e.g., 'Conference Room A')")
    capacity = models.IntegerField(help_text="Maximum number of people the space can accommodate")
    location = models.CharField(max_length=255, help_text="Physical location or address of the space")
    
    # Image fields for the space
    image1 = models.ImageField(upload_to='space_images/', blank=True, null=True, 
                               help_text="First image of the space")
    image2 = models.ImageField(upload_to='space_images/', blank=True, null=True, 
                               help_text="Second image of the space")
    image3 = models.ImageField(upload_to='space_images/', blank=True, null=True, 
                               help_text="Third image of the space")
    
    # Status field to indicate if the space is currently booked
    is_booked = models.BooleanField(default=False, help_text="Indicates if the space is currently booked")

    class Meta:
        verbose_name = "Space"
        verbose_name_plural = "Spaces"
        ordering = ['name'] # Order spaces by name by default

    def __str__(self):
        """String representation of the Space object."""
        status = "Booked" if self.is_booked else "Free"
        return f"{self.name} ({self.capacity} capacity) - {status}"

    def get_status_display(self):
        """Returns a user-friendly string for the booking status."""
        return "Booked" if self.is_booked else "Free"