
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from Books.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields = ['book_name', 'pages', 'price','author']

        def validate(self,data):
            print(data)
            price = data.get('price')
            if price<50:
                msg = "data > 50"
                raise exceptions.ValidationError('msg')
            return data


