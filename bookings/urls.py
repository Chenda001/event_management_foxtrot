from django.urls import path
from . import views
app_name = 'bookings'


urlpatterns = [
    path('book/', views.view_booking, name='view_booking'),
]
