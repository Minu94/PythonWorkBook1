from django.db import models
class products(models.Model):
    name=models.CharField(max_length=10)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)
class offer(models.Model):
    code=models.CharField(max_length=16)
    description=models.CharField(max_length=200)
    discount=models.FloatField()



# Create your models here.
