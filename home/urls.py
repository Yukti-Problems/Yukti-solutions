from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('CollegeLogin', include('collegelogin.urls')),
    path('AdminLogin', include('adminlogin.urls')),
    path('nbaform', include('collegelogin.urls')),

    # path('CollegeLogin.html', views.collegelogin, name='college'),
    # path('AdminLogin.html', views.adminlogin, name='admin'),
]