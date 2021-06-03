from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    price=models.FloatField()
    pages=models.IntegerField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

 # books=Book.objects.all()
# book=Book.objects.get(id=1)
#  for bk in books:
#    ...:     print(bk)
# book=Book(book_name='neethu',price=20,pages=5,author='sini')

# In [6]: book.save()
#  books=Book.objects.filter(price=10)
# books=Book.objects.filter(price__lt=10) less than
# books=Book.objects.filter(price__lt=10) less than equal
# books=Book.objects.filter(price__gt=10) greater than
# books=Book.objects.filter(price__gte=10) grater than equal