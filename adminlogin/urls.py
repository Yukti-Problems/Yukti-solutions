from django.contrib import admin
from django.urls import path
from adminlogin import views

urlpatterns = [
    path('', views.adminlogin, name='adminlogin'),
]