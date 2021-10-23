from django.http.response import HttpResponse
from django.shortcuts import render, redirect

import books.views.book
from books.models import Book
import os

def home(request):
    # list books from DB
    books = Book.objects.all()
    # render the books on html page
    return  render(request, 'book/index.html', {
        'all_books' : books
    })
    # return HttpResponse('Hello from books index page')

def read(request):
    return HttpResponse('Hello from read page')

def create_book(request):
    return render(request,'book/create.html')

def save_book(request):
    if request.method == "POST":
        # print(request.POST)
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_desc')
        book_price = request.POST.get('book_price')
        is_home = 1 if ('is_home_visible' in request.POST) else 0
        # request.FILES#1
        if len(request.FILES) != 0:
            book_photo = request.FILES['myfile']
        # save image MEDIA_URL#2
        # in edit view old pic and upload new one#3
        # validate against task 2
        # save valid data to the database
        Book.objects.create(
            name=book_name,
            description=book_description,
            price=book_price,
            is_home=int(is_home),
            photo=book_photo
        )
        return redirect('book-list')

def edit_book(request,book_id):
    # get book old data from db
    book = Book.objects.get(pk=book_id)
    # request.session['book_id'] = book_id
    return render(request,'book/edit.html',{
        'book_data': book
    })
def save_edit_book(request,book_id):
    if request.method == "POST":
        # print(request.POST)
        # book_id = request.session['book_id']
        book = Book.objects.get(pk=book_id)
        book.name = request.POST.get('book_name')
        book.description = request.POST.get('book_desc')
        book.price = request.POST.get('book_price')
        # request.FILES#1
        if len(request.FILES) != 0:
            if len(book.photo.url) > 0:
                os.remove(book.photo.path)
            book.photo = request.FILES['mynewfile']
        # save valid data to the database
        book.save()
        return redirect('book-list')
    # Book.objects.filter(pk=book_id).update(
    #     name=book_name,
    #     description=book_description,
    #     price=book_price,
    #     photo=book_photo
    # )

def delete_book(request,book_id):
    Book.objects.get(pk=book_id).delete()
    # request.session['book_id'] = book_id
    return redirect('book-list')

def bulk_delete_books(request):
    # print(request.method)
    # return HttpResponse('test')
    if request.method == "POST":
        id_list = request.POST.getlist("selected_option[]")
        print(id_list)
        for book_id in id_list:
            Book.objects.get(pk=book_id).delete()
        return redirect('book-list')

    # Book.objects.raw('DELETE * FROM Book WHERE id IN (%s)', [','.join([id_list])])



