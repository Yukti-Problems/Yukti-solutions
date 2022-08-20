from django.contrib import admin
from django.urls import path, include
from collegelogin import views

urlpatterns = [
   path('', views.collegelogin, name='collegelogin'),
   path('/fornewbranch', views.fornewbranch, name='fornewbranch'),
   path('nbaform', views.nbaform, name='nbaForm'),

]