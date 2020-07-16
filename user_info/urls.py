from django.urls import path

from . import views

urlpatterns = [
    path('demo/<int:usr_id>/', views.profile, name='profile'),
    path('getUser/', views.getUser, name='Get User API'),
    path('register/', views.register, name='Register API')
]
