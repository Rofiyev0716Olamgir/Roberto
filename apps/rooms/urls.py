from django.urls import path
from .views import room_list, room_detail

app_name = 'rooms'

urlpatterns = [
    path('rooms_list/', room_list, name='rooms_list'),
    path('rooms/<slug:slug>/', room_detail, name='room_detail'),
]

