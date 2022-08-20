from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('CollegeLogin.html', views.collegelogin, name='college'),
    path('AdminLogin.html', views.adminlogin, name='admin'),
]