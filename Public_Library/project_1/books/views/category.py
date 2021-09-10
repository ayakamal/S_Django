from books.models import Category
from django.views.generic import ListView

class CategoryList(ListView):
    template_name = 'category/index.html'
    model = Category
    # context_object_name = 'categories'