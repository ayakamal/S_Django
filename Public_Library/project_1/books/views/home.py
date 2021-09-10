from django.shortcuts import render
from books.models import Book
import os

def index(request):
    # books = Book.objects.all()
    books = Book.objects.filter(is_home=1, price__gt=0)
    return render(request,'home/index.html', {
        'all_books' : books
    })
    # return HttpResponse('Hello from index page')