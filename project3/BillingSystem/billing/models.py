from django.db import models

# Create your models here.


class Products(models.Model):
    product_name=models.CharField(max_length=120,unique=True)

    def __str__(self):

        return self.product_name


class Purchase(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    qty=models.IntegerField(null=False)
    purchase_price=models.IntegerField(null=False)
    selling_price=models.FloatField(null=False)
    purchase_date=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.qty+self.selling_price)


class Order(models.Model):
    billnumber=models.CharField(max_length=12,unique=True)
    bill_date=models.DateField(auto_now=True)
    customer_name=models.CharField(max_length=60)
    phone_number=models.CharField(max_length=12)
    bill_total=models.FloatField(default=0)

    def __str__(self):
        return str(self.billnumber)+str(self.customer_name)


class OrderLines(models.Model):
    bill_number=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_name=models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty=models.FloatField()
    amount=models.FloatField()

    def __str__(self):
        return str(self.bill_number)



