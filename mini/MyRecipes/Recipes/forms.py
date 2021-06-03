from django.forms import ModelForm
from .models import Recipe
from django import forms

class RecipeForm(ModelForm):
    ingredients=forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Recipe
        fields=['recipe_name','ingredients','category','recipe_img',
                'created_by'
                ]
