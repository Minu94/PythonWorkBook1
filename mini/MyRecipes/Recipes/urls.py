from django.urls import path

from . import views
app_name="recipes"


urlpatterns=[path('create',views.create_recipe,name="createrecipe"),
             path('listrecipe',views.list_recipes,name="listrecipe"),
             path('edit/<int:id>',views.edit_recipe,name="edit"),
             path('view/<int:id>',views.view_recipe,name="view"),
             path('delete/<int:id>',views.delete_recipe,name="delete"),
             path("search",views.searchRecipe,name="search")

]
