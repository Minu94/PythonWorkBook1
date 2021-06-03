from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AddEmpForm, EmpLoginForm

# Create your views here.


class AddUser(TemplateView):
    form_class = AddEmpForm
    template_name = "users/addemp.html"
    context = {}

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form .save()
            self.context["form"]=self.form_class()
            return render(request,self.template_name)
        else:
            self.context["form"] = form
            return render(request, self.template_name,self.context)


class EmpLogin(TemplateView):
    form_class = EmpLoginForm
    template_name = "users/emplogin.html"
    context = {}

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request,self.template_name,self.context)





