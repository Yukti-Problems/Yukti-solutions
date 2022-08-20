from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def collegelogin(request):
    return render(request, "CollegeLogin.html")
    
def adminlogin(request):
    return render(request, "AdminLogin.html")