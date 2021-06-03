from django.contrib import admin
from .models import Order, OrderLines

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderLines)