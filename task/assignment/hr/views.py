from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Country,State,District, City, Person
from .forms import AddPersonForm
# Create your views here.


class AddPerson(TemplateView):
    model = Person
    form_class = AddPersonForm
    template_name = "hr/person.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context['form'] = self.form_class()
        return render(request,self.template_name,self.context)


def unread(request):

    if request.method=='POST':
        count=request.POST['country']
        print("hello")
        print("count status ",count)