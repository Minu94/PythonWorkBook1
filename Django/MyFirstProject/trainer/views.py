from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def trainerreg(request):
    return render(request,'trainer/registration.html')


def trainerlogin(request):
    return render(request,'trainer/login.html')