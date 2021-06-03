import django_filter

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model=Recipe
        fields="__all__"
        exclude=['recipe_img']

