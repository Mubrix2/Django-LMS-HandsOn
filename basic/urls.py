from django.urls import path
from . import views

urlpatterns = [ 
 path('login/', views.loginPage, name='login'),
 path('logout/', views.logoutUser, name='logout'),
 path('register/', views.registerPage, name='register'),
 path('profile/<str:pk>', views.userProfile, name='user-profile'),

 path('', views.home, name='home'),
 path('room/<int:pk>', views.room, name='room'),

 path('create-room/', views.create_room, name='create-room'),
 path('update-form/<str:pk>', views.updateRoom, name='update-room'),
 path('delete-form/<str:pk>', views.deleteRoom, name='delete-room'),
 path('delete-message/<str:pk>', views.deleteMessage, name='delete-message')
]