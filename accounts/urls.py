from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Default to login view
    path('bookings/', views.bookings_view, name='bookings'),
    path('events/', views.events_view, name='events'),
    path('venues/', views.venues_view, name='venues'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
