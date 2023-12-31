from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.hello_world, name='home'),
    path('api/facebook/<int:room_number>/', views.FacebookRoomView.as_view(), name='FaceBook-Room'),
    path('api/google/<int:room_number>/', views.GoogleRoomView.as_view(), name='Google-Room'),
    path('api/amazon/<int:room_number>/', views.GoogleRoomView.as_view(), name='Amazon-Room'),
    path('api/netflix/<int:room_number>/', views.GoogleRoomView.as_view(), name='Netflix-Room'),
    path('api/hulu/<int:room_number>/', views.GoogleRoomView.as_view(), name='Hulu-Room'),
    path('api/rooms/', views.AllRoomView.as_view(), name='all-rooms'),
    path('search/', views.EndTimeFilterView.as_view()),
    path('api/migration', views.migration)
]
