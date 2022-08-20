from contextlib import redirect_stderr
import email
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth

# Create your views here.

def collegelogin(request):
    return render(request, "CollegeLogin.html")

def fornewbranch(request):
    return render(request, "nbaNewBranch.html")

def nbaform(request):
    return render(request, "nbaForm.html")