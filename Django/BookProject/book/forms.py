from django import forms


class BookCreateForm(forms.Form):
    bookname=forms.CharField(max_length=100)
    price=forms.FloatField()
    pages=forms.IntegerField()
    author=forms.CharField(max_length=100)
