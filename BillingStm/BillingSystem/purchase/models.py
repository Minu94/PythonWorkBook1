from django.db import models
from products.models import Products, ProductPrice


# Create your models here.

class Order(models.Model):
    bill_number = models.CharField(max_length=120,unique=True)
    bill_date = models.DateField(auto_now=True)
    customer_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12)
    bill_total = models.FloatField(default=0)

    def __str__(self):
        return self.bill_number


class OrderLines(models.Model):
    bill_number = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty = models.FloatField()
    product_price = models.ForeignKey(ProductPrice,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_name)+str(self.bill_number)


