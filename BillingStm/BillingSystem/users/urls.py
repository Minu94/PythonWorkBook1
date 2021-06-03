from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('addemp',views.AddUser.as_view(),name="addemp"),
               path('loginemp',views.EmpLogin.as_view(),name="loginemp"),
]
