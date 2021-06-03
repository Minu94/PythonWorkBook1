from django.forms import ModelForm
from django import forms
from .models import Products, Purchase, Order,\
    OrderLines


class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"


class AddPurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
        widgets = {'qty':forms.TextInput(attrs=({'class':'form-control'}))}

class OrderForm(ModelForm):

    # billnumber = forms.CharField(widget = forms.TextInput(attrs=({'class':'form-control'})))
    class Meta:

        model = Order
        fields=['billnumber','customer_name','phone_number']


class OrderLineForm(forms.Form):
    bill_number = forms.CharField(max_length=12)
    queryset = Purchase.objects.all().values_list('product__product_name',flat=True)
    choices =[(name,name) for name in queryset]
    product_name = forms.ChoiceField(choices=choices,required=False,widget=forms.select())
    product_qty = forms.IntegerField()

    class Meta:
        model = OrderLines
        fields = ['bill_number','product_name','product_qty']

