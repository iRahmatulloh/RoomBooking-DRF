from django.urls import path

from .views import hello_world, FacebookRoomView

urlpatterns = [
    path('api/', hello_world, name='home'),
    path('api/facebook/<int:room_number>/', FacebookRoomView.as_view(), name='FaceBook-Room'),
]
