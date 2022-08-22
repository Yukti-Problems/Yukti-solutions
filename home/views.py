from django.shortcuts import render, HttpResponse, redirect
from home.models import Clogin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    return render(request, "index.html")


# college works starts here

def collegelogin(request):
    if request.method=="POST":
        cid = request.POST.get('cid')
        password = request.POST.get('password')
        print(cid, password)

        # check if user has entered correct credentials
        user = authenticate(username=cid, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("nbaForm.html")

        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid Credentials!')
            return render(request, 'CollegeLogin.html')

    return render(request, 'CollegeLogin.html')

def nbaForm(request):
    return render(request, "nbaForm.html")

def nbaCurrentBranch(request):
    return render(request, "nbaCurrentBranch.html")
    
def nbaNewBranch(request):
    return render(request, "nbaNewBranch.html")

def nbaReapproval(request):
    return render(request, "nbaReapproval.html")


# Admin works starts here
def adminlogin(request):
    return render(request, "AdminLogin.html")
