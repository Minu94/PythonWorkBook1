
from . import views
from django.urls import path

urlpatterns = [
    path('trainerreg/',views.trainerreg,name='TrainerRegistration'),
    path('trainerlogin/',views.trainerlogin,name='TrainerLogin')
]
