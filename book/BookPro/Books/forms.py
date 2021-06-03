from .models import Book
from django.forms import ModelForm

#form for class based customization


class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"


