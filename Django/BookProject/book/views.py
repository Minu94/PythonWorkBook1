from django.shortcuts import render,redirect
from .models import Book
from .forms import BookCreateForm


# Create your views here.

def createbook(request):
    form=BookCreateForm()
    context={}
    context['form']=form
    if request.method== 'POST':
        form=BookCreateForm(request.POST)
        if form.is_valid():
            bookname = form.cleaned_data.get("bookname")
            price=form.cleaned_data.get('price')
            author=form.cleaned_data.get('author')
            pages=form.cleaned_data.get('pages')
            print(bookname,",",pages,",",price,",",author)
            book = Book(book_name=bookname, price=price, pages=pages, author=author)
            book.save()
            return redirect('getbooks')
    return render(request,'book/createbook.html',context)


#
# def insertbook(request):
#     bookname=request.POST.get("bname")
#     price=request.POST.get('price')
#     author=request.POST.get('author')
#     pages=request.POST.get('pages')
#     print(bookname,",",pages,",",price,",",author)
#     book=Book(book_name=bookname,price=price,pages=pages,author=author)
#     book.save()
#     return redirect('getbooks')
def getbooks(request):
    books=Book.objects.all()
    context={}
    context['books']=books
    return render(request,'book/listbooks.html',context)