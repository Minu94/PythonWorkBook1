from django.db import models

# Create your models here.


class Mpin(models.Model):
    mpin = models.IntegerField(primary_key=True,unique=True)


class Register(models.Model):
    user_name = models.CharField(max_length=120,unique=True)
    user_password = models.CharField(max_length=120)
    mobile_num = models.IntegerField()
    email_id = models.CharField(max_length=120)
    mpin = models.ForeignKey(Mpin,on_delete=models.CASCADE)
    aadhar = models.IntegerField()


