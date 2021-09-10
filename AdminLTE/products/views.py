from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Product,Category
from django.views.generic import ListView
import os

# Create your views here.

def index(request):
    # books = Book.objects.all()
    # books = Book.objects.filter(is_home=1, price__gt=0)
    # return render(request,'home/index.html', {
    #     'all_books' : books
    # })
    return  render(request,'home/index.html')
    # return HttpResponse('Hello from index page')

def home(request):
    # list products from DB
    products = Product.objects.all()
    # render the products on html page
    return  render(request, 'product/index.html', {
        'all_products' : products
    })
    # return render(request, 'product/index.html')
    # return HttpResponse('Hello from products index page')

def add_product(request):
    return render(request,'product/add.html',{'all_categories' : Category.objects.all()})
    # return HttpResponse('Hello from products index page')

def save_product(request):
    if request.method == "POST":
        # print(request.POST)
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_desc')
        product_price = request.POST.get('product_price')
        # request.FILES#1
        if len(request.FILES) != 0:
            product_photo = request.FILES['myImage']
        product_category = request.POST.get('product_category')
        if product_name == '' or product_price == '' or product_description == '':
            return HttpResponse('All fields are required')
        elif int(product_price) <= 0:
            return HttpResponse('product price must be greater than 0')
        elif product_description.isdigit():
            return HttpResponse('product description must be text')

        for product in Product.objects.all():
            if product.name == product_name:
                return HttpResponse('This book aleady exists')

                # save image MEDIA_URL#2
        # in edit view old pic and upload new one#3
        # validate against task 2
        # save valid data to the database
        Product.objects.create(
            name=product_name,
            description=product_description,
            price=product_price,
            photo=product_photo,
            category=Category.objects.get(name=product_category)
        )
        return redirect('product-list')

def edit_product(request,product_id):
    product = Product.objects.get(pk=product_id)
    return render(request,'product/edit.html',{
        'product_data': product,'all_categories' : Category.objects.all()
    })
def save_edit_product(request,product_id):
    if request.method == "POST":
        # print(request.POST)
        product = Product.objects.get(pk=product_id)
        product.name = request.POST.get('product_name')
        product.description = request.POST.get('product_desc')
        product.price = request.POST.get('product_price')
        # request.FILES#1
        if len(request.FILES) != 0:
            if len(product.photo.url) > 0:
                os.remove(product.photo.path)
            product.photo = request.FILES['myImage']
        else:
            product.photo = Product.objects.get(pk=product_id).photo

        if request.POST.get('product_category'):
            product_category = request.POST.get('product_category')
            product.category = Category.objects.get(name=product_category)
        else:
            product.category = Product.objects.get(pk=product_id).category

        if product.name == '' or product.price == '' or product.description == '':
            return HttpResponse('All fields are required')
        elif float(product.price) <= 0:
            return HttpResponse('product price must be greater than 0')
        elif product.description.isdigit():
            return HttpResponse('product description must be text')
        # save valid data to the database
        product.save()
        return redirect('product-list')

class CategoryList(ListView):
    template_name = 'category/index.html'
    model = Category
    context_object_name = 'categories'

def add_category(request):
    return render(request,'category/addcategory.html')

def save_category(request):
    if request.method == "POST":
        # print(request.POST)
        product_category = request.POST.get('product_category')
        Category.objects.create(
            name=product_category,
        )
        return redirect('category-list')

def delete_product(request,product_id):
    Product.objects.get(pk=product_id).delete()
    return redirect('product-list')

def bulk_delete_product(request):
    # print(request.method)
    # return HttpResponse('test')
    if request.method == "POST":
        id_list = request.POST.getlist("selected_product[]")
        print(id_list)
        for product_id in id_list:
            Product.objects.get(pk=product_id).delete()
        return redirect('product-list')