from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm, AddExpensesForm,ReviewExpenseForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Expenses
from django.db.models import Sum,Aggregate
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form=RegistrationForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')
        else:
            print('er')
    return render(request,'registration.html',context)

def signin(request):
    form=LoginForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request, 'home.html', context)
            else:
                return render(request, 'login.html', context)


    return render(request,'login.html',context)

def signOut(request):
    logout(request)
    return redirect(signin)
@login_required
def editProfile(request):
    user=User.objects.get(username=request.user)
    form = RegistrationForm(instance=user)
    context={}
    context['form']= form
    if request.method=='POST':
        form=RegistrationForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form']=form
            return render(request, 'editProfile.html', context)


    return render(request,'editProfile.html',context)

def userHome(request):
    return render(request,'home.html')


@login_required #edit settings add login url otherwise lead to client error 404 so to direct to loginpage from add
def addExpenses(request):
    form=AddExpensesForm(initial=request.user)
    context={}
    context['form']=form
    expenses=Expenses.objects.filter(user=request.user)
    context['expenses']=expenses
    if request.method=='POST':
        form=AddExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'add')

    return render(request,'expences.html',context)

@login_required
def editExpenses(request,pk):
    expenses=Expenses.objects.get(id=pk)
    form=AddExpensesForm(instance=expenses)
    context={}
    context['form']=form
    if request.method=='POST':
        form=AddExpensesForm(instance=expenses,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'add')
        else:
            context['form']=form
            return render(request,'editexpenses.html',context)

    return render(request,'editexpenses.html',context)
@login_required
def deleteexpenses(request,pk):
    try:
        expenses=Expenses.objects.get(id=pk).delete()
        return redirect(request,'add')
    except Exception as e:
        return redirect(request, 'add')

@login_required
def review_expense(request):
    form=ReviewExpenseForm(initial={'user':request.user}) #to get username in hidden field
    context={}
    context['form']=form
    if request.mathod=='POST':
        form =ReviewExpenseForm(request.POST)
        if form.is_valid():
            frmdate=form.cleaned_data.get('from_date')
            todate=form.cleaned_data.get('to_date')
            print(frmdate,',',todate)
            expenses=Expenses.objects.filter(date__gte=frmdate,date__lte=todate,user=request.user)
            total = Expenses.objects.filter(date__gte=frmdate, date__lte=todate, user=request.user).aggregate(Sum('amount'))
            context['expenses']=expenses
            # total=0
            # for e in exp:
            #     total+=e['amount']
            context['total']=total
            return render('reviewexpense.html', context)

    return render('reviewexpense.html',context)
