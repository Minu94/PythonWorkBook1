from django import forms
from django.forms import ModelForm
from .models import Country,State,District, City, Person
# from smart_selects import views


class AddPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"





