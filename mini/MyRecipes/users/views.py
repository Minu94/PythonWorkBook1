from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,ProfileForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Profile
# Create your views here.

def register(request):
    form=UserRegistrationForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signIn')
    return render(request,'users/registration.html',context)

def home(request):
    return render(request,'users/home.html')


def create_profile(request):
    form=ProfileForm(initial={"user":request.user})
    context={}
    context['form']=form
    if request.method=='POST':
        form=ProfileForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form']=form
            return render(request, 'users/createprofile.html', context)

    return render(request,'users/createprofile.html',context)

# profile.objects.all().delete()
# profile.objects.all().count()

def signIn(request):
    form=LoginForm()
    context={}
    context['form']=form
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,'users/home.html')
            else:
                return render(request,'users/login.html',context)
    return render(request,'users/login.html',context)

def signOut(request):
    logout(request)
    return redirect('signIn')

def edit_profile(request):
    user=Profile.objects.get(user=request.user)
    form=ProfileForm(initial={"user":request.user},instance=user)
    context={}
    context['form']=form
    if request.method=='POST':
        form=ProfileForm(instance=user,data=request.post,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form']=form
            return render(request, 'users/editprofile.html', context)
    return render(request,'users/editprofile.html',context)


def view_profile(request):
    user=Profile.objects.all(user=request.user)
    context={}
    context['user']=user
    return render(request,'users/viewprofile.html',context)
from .filter import RecipeFilter
def searchRecipes(request):
    recipes=Recipe.objects.all()
    myfilter=RecipeFilter(request.get,queryset=recipes)
    recipes=myfilter.qs #queryset
    context={}
    context['recipe']=recipes
    context['myfilter']=myfilter
    return render(request,"recipes/recipes_search.html",context)
