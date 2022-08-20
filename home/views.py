from contextlib import redirect_stderr
import email
# from ssl import _PasswordType
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, "index.html")

# def collegelogin(request):
#     return render(request, "CollegeLogin.html")
    
# def adminlogin(request):
#     return render(request, "AdminLogin.html")





    # if request.method=='POST':
    #     email1=request.POST['email']
    #     password1=request.POST['password']
    #     x=auth.authenticate(email=email1,password=password1)
    #     if x is None:
    #         return redirect("CollegeLogin.html")
    #     else:
    #         return redirect('/')
    # else:

    # if request.method=='POST':
    #     email1=request.POST['email']
    #     password1=request.POST['password']
    #     x=auth.authenticate(email=email1,password=password1)
    #     if x is None:
    #         auth.login(request,email)
    #         return redirect("AdminLogin.html")
    #     else:
    #         return redirect('/')
    # else: