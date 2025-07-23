from django.urls import path
from . import views

app_name = 'bookings'


urlpatterns = [
    path('booking_list/', views.booking_list, name='booking_list'),
]
