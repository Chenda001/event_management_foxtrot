from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('view/', views.booking_list, name='booking_list'),
    path('book/<int:space_id>/', views.book_space, name='book_space'),
]
