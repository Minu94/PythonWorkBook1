from django.db import models

# Create your models here.


class Employee(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=80)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return self.username


class EmpLogin(models.Model):
    username = models.CharField(max_length=100)
    password =models.CharField(max_length=80)
    login_time = models.DateTimeField(auto_now=True)
    logout_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login_time


