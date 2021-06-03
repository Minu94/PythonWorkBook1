from django.db import models

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=120)
    product_id = models.CharField(max_length=120)

    def __str__(self):
        return self.product_name


class ProductPrice(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    initial_qty = models.IntegerField()
    cost_price = models.FloatField()
    used_qty = models.IntegerField(default=0)
    discount = models.IntegerField()
    marked_price = models.FloatField()

    def __str__(self):
        return str(self.marked_price)


