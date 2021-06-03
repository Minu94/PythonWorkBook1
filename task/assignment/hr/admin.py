from django.contrib import admin
from .models import *

# Register your models here.
my_models = [Country, State, District, City, Person]
admin.site.register(my_models)
