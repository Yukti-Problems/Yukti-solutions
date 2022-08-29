from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('StudentLogin.html', views.studentlogin, name='student'),
    path('AdminLogin.html', views.adminlogin, name='admin'),
    path('StudentSignup.html', views.studentsignup, name='students'),
    path('StudentInput.html', views.studentinput, name='studenti'),
    path('AdminInput.html', views.admininput, name='admini'),
]