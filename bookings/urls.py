from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('view/', views.view_bookings, name='view_bookings'),
]
