from django.db import models
# from smart_selects.db_fields import ChainedForeignKey

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=120)

    def __str__(self):
        return self.country


class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state = models.CharField(max_length=120)

    def __str__(self):
        return self.state


class District(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    district = models.CharField(max_length=120)

    def __str__(self):
        return self.district


class City(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    city = models.CharField(max_length=120)

    def __str__(self):
        return self.city


class Person(models.Model):
    name = models.CharField(max_length=120)
    birth_date = models.DateField()
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    state = models.ForeignKey(State,
                              on_delete=models.SET_NULL,null=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,null=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name


