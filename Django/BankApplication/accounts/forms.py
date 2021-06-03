from django import forms
from django.forms import ModelForm
from .models import TransferDetails,Account


class AccountCreateForm(forms.Form):
    personname=forms.CharField(max_length=100)
    accno=forms.CharField(max_length=15)
    actype=forms.CharField(max_length=120)
    balance=forms.IntegerField()
    phonenumber=forms.CharField(max_length=12)
    mpin=forms.CharField(max_length=6)


class LoginForm(forms.Form):
    phonenumber = forms.CharField(max_length=12)
    mpin = forms.CharField(max_length=6)

class BalanceCheck(forms.Form):
    mpin = forms.CharField(max_length=6)
    def clean(self):
        cleaned_data = super().clean()
        mpin = cleaned_data.get('mpin')
        try:
            object=Account.objects.get(mpin='mpin')
            if(object):
                pass
        except:
            msg="invalid"
            self.add_error('mpin',msg)


class TransferAmountForm(ModelForm):

    class Meta:
        model=TransferDetails
        fields="__all__"
        # fields=("mpin",) if only one needed

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get('mpin')
        acno = cleaned_data.get('accno')
        amount = cleaned_data.get('amount')
        # try:
        #     object=Account.objects.get(mpin='mpin')
        #     if(object):
        #         pass
        # except:
        #     msg="invalid"
        #     self.add_error('mpin',msg)
        try:
            object=Account.objects.get(accno='acno')
            if(object):
                if(object.balance<amount):
                    msg='insufficient'
                    self.add_error('amount',msg)

                pass
        except:
            msg="invalid"
            self.add_error('accno',msg)


