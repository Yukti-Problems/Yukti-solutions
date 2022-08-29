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

#Student Work Starts here

def studentlogin(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            email = request.POST.get('email')
            request.session['email'] = email
            password = request.POST.get('password')
            print(email,password)


            if email == 'admin' and password == 'admin':
                messages.warning(request, 'Please login here!')
                context = {"variable" : "warning"}
                return redirect("AdminLogin.html",context)

            # try:
            #     details = Student_Details.objects.get(email=email)
            # except:
                # No backend authenticated the credentials
                # print("hi")
                # messages.error(request, 'Please Signup First!')
                # context = {"variable" : "warning"}
                # return render(request, 'StudentSignup.html',context)

            # check if user has entered correct credentials
            user = authenticate(username=email, password=password)

            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("StudentInput.html")

            else:
                # No backend authenticated the credentials
                messages.error(request, 'Invalid Credentials!')
                context = {"variable" : "danger"}
                return render(request, 'StudentLogin.html',context)

    else: 
        logout(request)
        return redirect("StudentLogin.html")

    return render(request, 'StudentLogin.html')

def studentsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    conpass = request.POST.get('conpass')
    if password != conpass:
        messages.error(request, 'Please Enter same password on the same fields!')
        context = {"variable" : "warning"}
        return render(request, 'StudentSignup.html',context)
    else:
        try:
            details = Student_Details.objects.get(email=email)
        except:
            # No backend authenticated the credentials
            messages.error(request, 'Please use another email id First!')
            context = {"variable" : "warning"}
            return render(request, 'StudentSignup.html',context)

        studet = Student_Details(name=name, email=email, phone=phone, password=password)
        studet.save()
        user = User.objects.create_user(cid, cid+'@gmail.com', password)
        user.save()
        user = authenticate(username=email, password=password)
        login(request, user)
        messages.success(request, 'Please Login now!')
        context = {"variable" : "warning"}
        return render(request, "StudentLogin.html",context)

def studentinput(request):
    return render(request, "StudentInput.html")


# Admin work Starts here

def adminlogin(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            username = request.POST.get('Username')
            password = request.POST.get('password')
            # print(email, password)

            # check if user has entered correct credentials
            user = authenticate(username=username, password=password)

            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("AdminInput.html")

            else:
                # No backend authenticated the credentials
                messages.error(request, 'Invalid Credentials!')
                context = {"variable" : "danger"}
                return render(request, 'AdminLogin.html',context)


    else: 
        logout(request)
        return redirect("AdminLogin.html")

    return render(request, 'AdminLogin.html')

def admininput(request):
    return render(request, "AdminInput.html")