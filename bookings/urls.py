from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.create_booking, name='create_booking'),
    path('venues/', views.venue_list, name='venue_list'),
]
