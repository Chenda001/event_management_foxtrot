from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
]
