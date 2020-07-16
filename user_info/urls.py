from django.urls import path

from . import views

urlpatterns = [
    path('demo/<int:usr_id>/', views.profile, name='profile'),
    path('getUser/', views.getUser, name='Get User API'),
    path('getUserInfo/', views.getUserInfo, name='Get User Partial API'),
    path('register/', views.register, name='Register API')
]
