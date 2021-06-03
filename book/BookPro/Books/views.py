from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.

#listview
#Detailview
#deleteview
#updateview


# class BookCreate(CreateView):
#     model=Book
#     fields="__all__"
#     template_name="Books/book_form.html"
#     success_url= reverse_lazy('list')
#
# class BookList(ListView):
#     model= Book
#     context_object_name="books"
#     template_name="Books/book_list.html"

# class BookEdit(UpdateView):
#     model=Book
#     fields="__all__"
#     success_url= reverse_lazy("list")
#     template_name="Books/book_edit.html"


class BookView(DetailView):
    model = Book
    context_object_name="book"
    template_name="Books/book_detail.html"

#
# class BookDelete(DeleteView):
#     model = Book
#     context_object_name = "book"
#     template_name = "Books/book_delete.html"
#     success_url = reverse_lazy("list")

# class customization
from .forms import BookCreateForm
class BookCreate(TemplateView):
    form_class=BookCreateForm()
    template_name='Books/book_form.html'
    context={}
    def get(self,request,*args,**kwargs):
        form=BookCreateForm()
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')


class BookList(TemplateView):
    model=Book
    template_name="Books/book_list.html"
    context={}

    def get_query_set(self):
        return self.model.Objects.all()

    def get(self,request,*args,**kwargs):
        self.context['books']=self.get_query_set()
        return render(request,self.template_name,self.context)


class BookEdit(TemplateView):
    model=Book
    template_name="Books/book_edit.html"
    context={}

    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self,request,*args,**kwargs):
        book=self.get_query_set(kwargs.get("pk"))
        form=BookCreateForm(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        book = self.get_query_set(kwargs.get("pk"))
        form=BookCreateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

class BookDelete(TemplateView):
    model=Book
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("pk"))
        book.delete()
        return redirect("list")


    #request to server for data get
    # we send data to server post

#function based views
#class based view
#class based customize
#rest

