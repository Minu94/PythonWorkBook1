from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . models import Products, Purchase, Order, OrderLines
from .forms import AddProductForm, AddPurchaseForm,\
    OrderForm, OrderLineForm

# Create your views here.
# billing/addproduct


class AddProduct(TemplateView):
    form_class = AddProductForm()
    model = Products
    context = {}
    template_name = "billing/addproduct.html"

    def get(self,request,*args,**kwargs):
        self.context['form']=self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listproduct')

        else:
            self.context['form']=form
            return render(request, self.template_name, self.context)


# billing/listproduct

class ListProduct(TemplateView):
    model = Products
    template_name = 'billing/listproduct.html'
    context = {}

    def get(self,request,*args,**kwargs):
        products=Products.objects.all()
        self.context['products']=products
        return render(request,self.template_name,self.context)

#billing/editproduct

class EditProduct(TemplateView):
    model = Products
    template_name = 'billing/editproduct.html'
    context = {}

    def get_object(self,id):
        return Products.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        product = self.get_object(kwargs.get('pk'))
        form = AddProductForm(instance=product)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        product = self.get_object(kwargs.get('pk'))
        form = AddProductForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('listproduct')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

#billing/delete


class DeleteProduct(TemplateView):
    model=Products

    def get_object(self,id):
        return Products.objects.get(id=id)

    def get(self,request,*args,**kwargs):
        product= self.get_object(kwargs.get('pk'))
        product.delete()
        return redirect('listproduct')

# billing/addpurchase


class AddPurchase(TemplateView):
    form_class=AddPurchaseForm()
    model=Purchase
    context={}
    template_name="billing/addpurchase.html"

    def get(self,request,*args,**kwargs):
        self.context['form']=self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=AddPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listpurchase')

        else:
            self.context['form']=form
            return render(request, self.template_name, self.context)



#billing/listpurchase

class ListPurchase(TemplateView):
    model = Purchase
    template_name = 'billing/listpurchase.html'
    context = {}

    def get(self,request,*args,**kwargs):
        purchases=Purchase.objects.all()
        self.context['purchases']=purchases
        return render(request,self.template_name,self.context)


#billing/editpurchase

class EditPurchase(TemplateView):
    model = Purchase
    template_name = 'billing/editpurchase.html'
    context = {}

    def get_object(self,id):
        return Purchase.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        purchase = self.get_object(kwargs.get('pk'))
        form = AddPurchaseForm(instance=purchase)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        purchase = self.get_object(kwargs.get('pk'))
        form = AddPurchaseForm(instance=purchase,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('listpurchase')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

#billing/deletepurchase


class DeletePurchase(TemplateView):
    model=Purchase

    def get_object(self,id):
        return Purchase.objects.get(id=id)

    def get(self,request,*args,**kwargs):
        purchase= self.get_object(kwargs.get('pk'))
        purchase.delete()
        return redirect('listpurchase')

#billing/order

class OrderView(TemplateView):
    model= Order
    template_name="billing/order.html"
    context={}

    def get(self,request,*args,**Kwargs):
        order = Order.objects.all().last()
        billnumber = int(order.billnumber)
        billnumber = str(billnumber)
        form = OrderForm(initial={'billnumber':billnumber})
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = OrderForm(request.POST)
        self.context['form'] = form
        if form.is_valid():
            billnum = form.cleaned_data.get("billnumber")
            form.save()
            return redirect('orderlines',billno=billnum)
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class OrderLineView(TemplateView):
    model = OrderLines
    template_name= "billing/orderlines.html"

    def get(self,request,*args,**kwargs):
        billnum = kwargs.get("billnum")
        form = OrderLineForm(initial={'bill_number':billnum})
        self.context['form'] = form
        return render(request,self.template_name, self.context )

    def post(self,request,*args,**kwargs):
        form = OrderLineForm(request.POST)
        if form.is_valid():
            billnum=form.cleaned_data.get("bill_number")
            product_name=form.cleaned_data.get("product_name")
            product_qty=form.cleaned_data.get("product_qty")
            return render(request,self.template_name,self.context)



