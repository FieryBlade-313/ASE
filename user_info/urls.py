from django.urls import path

from . import views

urlpatterns = [
    path('demo/<int:usr_id>/', views.profile, name='profile'),
    path('getUser/', views.getUser, name='Get User API'),
    path('getUserInfo/', views.getUserInfo, name='Get User Partial API'),
    path('register/', views.register, name='Register API'),
    path('login/', views.login, name='Login API'),
    path('bulkJob/', views.createBulkJob, name='Bulk Job API'),
    path('connectBulkJob/', views.connectBulkJob, name='Bulk Job connector API'),
    path('jobsCategory/', views.getJobsByCategory, name='Jobs by Category API'),
    path('review/', views.review, name='Create Review API'),
    path('job/', views.createJob, name='Create Job API'),
    path('getJobsUser/', views.getJobsByUser, name='Get Job by User API')
    path('follows/', views.FollowsList.as_view(), name='Follow API'),
    path('foi/', views.FOIList.as_view(), name='Field Of Interest API'),
    path('review/', views.review, name='Create Review API')
