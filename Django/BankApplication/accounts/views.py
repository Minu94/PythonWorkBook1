from django.shortcuts import render,redirect
from .forms import AccountCreateForm,LoginForm, BalanceCheck, TransferAmountForm
from .models import Account

# Create your views here.

def createAccount(request):
    template_name='accounts/accountcreate.html'
    form=AccountCreateForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form= AccountCreateForm(request.POST)
        if form.is_valid():
            personname=form.cleaned_data.get("personname")
            accno = form.cleaned_data.get("accno")
            actype = form.cleaned_data.get('actype')
            balance = form.cleaned_data.get('balance')
            phonenumber = form.cleaned_data.get('phonenumber')
            mpin = form.cleaned_data.get('mpin')
            obj=Account(personname=personname,accno=accno,actype=actype, balance= balance,
                        phonenumber= phonenumber,mpin=mpin )
            obj.save()
            return render(request,template_name,context)



    return render(request,template_name,context)

def loginView(request):
    form = LoginForm()
    context = {}
    context['form'] = form
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            phone=form.cleaned_data.get('phonenumber')
            mpin=form.cleaned_data.get('mpin')
            try:
                object=Account.objects.get(phonenumber=phone)
                if (object.phonenumber==phone) & (object.mpin==mpin):
                    print("user exist")
                    return render(request,'accounts/accounthome.html')
            except Exception as e:
                print("inavalid")
                context['form']=form
                return render(request,'accounts/login.html',context)

    return render(request, 'accounts/login.html', context)

def balanceenq(request):
    form=BalanceCheck()
    context={}
    context['form']=form
    if request.method=='POST':
        form = BalanceCheck(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get('mpin')
            try:
                object=Account.objects.get(mpin=mpin)
                context['balance']=object.balance
                return render(request,'accounts/checkbalance.html',context)
            except Exception as e:
                context['form']=form
                return render(request, 'accounts/checkbalance.html', context)
    return render(request,'accounts/checkbalance.html',context)

def transfer(request):
    form=TransferAmountForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=TransferAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get('mpin')
            amount=form.cleaned_data.get('amount')
            try:
                object=Account.objects.get(mpin=mpin)
                bal=object.balance-amount
                object.balance=bal
                object.save()
            except Exception:
                context['form'] = form
                return render(request, 'accounts/checkbalance.html', context)

            form.save()
            return redirect('balance')
        else:
            context['form']=form
            return render(request, 'accounts/transferamount.html', context)
    return render(request,'accounts/transferamount.html',context)


def AccountActivity(request):
    form=BalanceCheck()
    context={}
    context['form']=form
    return render(request,'accounts/accounthistory.html',context)


#login,balance enquiry,account activity,transfer