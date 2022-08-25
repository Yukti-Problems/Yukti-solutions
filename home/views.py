from django.shortcuts import render, HttpResponse, redirect
from datetime import date
from home.models import College_Details
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

def index(request):
    return render(request, "index.html")


# college works starts here

def collegelogin(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            cid = request.POST.get('cid')
            request.session['cid'] = cid
            password = request.POST.get('password')
            s = SessionStore()
            s['cid'] = cid
            s.create()
            print(s.session_key)

            if cid == 'admin' and password == 'admin':
                messages.warning(request, 'Please login here!')
                context = {"variable" : "warning"}
                return redirect("AdminLogin.html",context)

            try:
                details = College_Details.objects.get(cid=cid)
            except:
                # No backend authenticated the credentials
                messages.error(request, 'Invalid Credentials!')
                context = {"variable" : "danger"}
                return render(request, 'CollegeLogin.html',context)

            # check if user has entered correct credentials
            user = authenticate(username=cid, password=password)

            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("nbaForm.html")

            elif details.Password == password:
                user = User.objects.create_user(cid, cid+'@gmail.com', password)
                user.save()
                user = authenticate(username=cid, password=password)
                login(request, user)
                return redirect("nbaForm.html")


            else:
                # No backend authenticated the credentials
                messages.error(request, 'Invalid Credentials!')
                context = {"variable" : "danger"}
                return render(request, 'CollegeLogin.html',context)

    else: 
        logout(request)
        return redirect("CollegeLogin.html")

    return render(request, 'CollegeLogin.html')

def nbaForm(request):
    if request.user.is_anonymous:
        messages.warning(request, 'Please Login First!')
        context = {"variable" : "warning"}
        return redirect("CollegeLogin.html",context) 

    cid = request.session['cid']
    details = College_Details.objects.get(cid=cid)
    print(details.nba_aggregated)
    return render(request, "nbaForm.html")

def nbaCurrentBranch(request):
    if request.user.is_anonymous:
        messages.warning(request, 'Please Login First!')
        context = {"variable" : "warning"}
        return redirect("CollegeLogin.html",context) 
    return render(request, "nbaCurrentBranch.html")
    
def nbaNewBranch(request):
    if request.user.is_anonymous:
        messages.warning(request, 'Please Login First!')
        context = {"variable" : "warning"}
        return redirect("CollegeLogin.html",context) 
    return render(request, "nbaNewBranch.html")

def nbaReapproval(request):
    if request.user.is_anonymous:
        messages.warning(request, 'Please Login First!')
        context = {"variable" : "warning"}
        return redirect("CollegeLogin.html",context) 
    return render(request, "nbaReapproval.html")


# Admin works starts here
def adminlogin(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            cid = request.POST.get('Username')
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
                context = {"variable" : "danger"}
                return render(request, 'AdminLogin.html',context)


    else: 
        logout(request)
        return redirect("AdminLogin.html")

    return render(request, 'AdminLogin.html')

