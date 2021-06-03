from django.contrib import admin
from .models import ProductPrice, Products

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductPrice)