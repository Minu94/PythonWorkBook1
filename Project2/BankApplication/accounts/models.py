from django.db import models
# from prototype.users.models import Mpin, Register

# Create your models here.

class Account(models.Model):
    mpin = models.ForeignKey('users.Mpin', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    accno = models.OneToOneField('users.Mpin',on_delete=models.CASCADE)
    actype = models.CharField(max_length=50)


