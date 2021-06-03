from django.shortcuts import render
from django.http import HttpResponse
from .models import products

# Create your views here.
def index(request):
    product=products.object.all()
    return render(request,'index.html',{'products':product})
    # return HttpResponse("<h1>welcome to django</h1>")
def about(request):
    return HttpResponse("<h1>about</h1>")
def contact(request):
    return HttpResponse("<h1>contacts</h1>")

