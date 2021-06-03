
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('studentreg/',views.studentreg,name='StudentRegistration'),
    path('studentlogin/',views.studentlogin,name='StudentLogin'),
    path('register/',views.getregdetails,name='details'),
    path('login/',views.getlogin,name='login')
]
