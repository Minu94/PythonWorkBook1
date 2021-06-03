from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def studentreg(request):
    return render(request,'student/registration.html')


def studentlogin(request):
    return render(request,'student/login.html')

def getregdetails(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    print(f"email: {email}\nPassword: {password}")
    return render(request,'student/login.html')

def getlogin(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    print(f"email: {email}\nPassword: {password}")
    context = {"email": email,"password":password}
    return render(request,'student/home.html',context)