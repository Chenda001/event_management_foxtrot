from django.urls import path
from . import views

app_name = 'venue'

urlpatterns = [
    # URL for viewing all spaces
    path('', views.space_list, name='space_list'),
    # URL for booking/unbooking a specific space
    path('book/<int:space_id>/', views.book_space, name='book_space'),
]
