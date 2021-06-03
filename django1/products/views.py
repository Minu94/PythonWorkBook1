from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    products=Products.objects.all()
    # return HttpResponse("<h1>welcome to django</h1>")
    return render(request,'index.html',{'products':products})

def about(request):
    return HttpResponse("<h1>about</h1>")


def contact(request):
    return HttpResponse("<h1>contact</h1>")


# Create your views here.
