from django.urls import path
from . import views


urlpatterns=[path("register", views.register, name="register"),
             path("login", views.signIn, name="signIn"),
             path("logout", views.signOut, name="signOut"),
             path('profile',views.create_profile,name="profile"),
             path('home',views.home,name='home'),
             path('editprofile',views.edit_profile,name='editprofile'),
             path('viewprofile',views.view_profile,name='viewprofile')

]
