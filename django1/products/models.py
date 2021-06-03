from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)
class offer(models.Model):
    code=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    discount=models.FloatField()