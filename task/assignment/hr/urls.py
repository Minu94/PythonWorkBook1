from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add',views.AddPerson.as_view(),name="add"),
    path('notification/',views.unread,name='unread')
]
