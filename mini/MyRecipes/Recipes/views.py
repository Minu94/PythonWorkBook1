from django.shortcuts import render,redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.

def create_recipe(request):
    form=RecipeForm(initial={'created_by':request.user})
    context={}
    context['form']=form
    if request.method=='POST':
        form = RecipeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listrecipe')
    return render(request,'Recipes/createrecipe.html',context)


def list_recipes(request):
    my_recipes=Recipe.objects.filter(created_by=request.user)
    context={}
    context['recipes']=my_recipes
    return render(request,'Recipes/myrecipes.html',context)


def edit_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    form= RecipeForm(instance=recipe)
    context={}
    context['form']=form
    if request.method=='POST':
        form= RecipeForm(instance=recipe,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listrecipe')
        else:
            return render(request, 'recipe/editrecipe.html', context)
    return render(request,'recipe/editrecipe.html',context)

def view_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    context={}
    context['recipe']=recipe
    return render(request,'recipe/recipeview.html',context)


def delete_recipe(request,id):
    Recipe.objects.get(id=id).delete()
    return redirect('listrecipes')


