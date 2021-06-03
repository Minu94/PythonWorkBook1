from django.shortcuts import render,redirect

# Create your views here.

def insertbook(request):
    bookname=request.POST.get("bname")
    price=request.POST.get('price')
    author=request.POST.get('author')
    pages=request.POST.get('pages')
    print(bookname,",",pages,",",price,",",author)
    # book=Book(book_name=bookname,price=price,pages=pages,author=author)
    # book.save()
    return redirect('getbooks')