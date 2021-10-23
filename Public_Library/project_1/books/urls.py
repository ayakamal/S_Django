from django.urls import path
from .views import home,read,index,create_book,save_book,edit_book,save_edit_book,delete_book,bulk_delete_books,CategoryList

urlpatterns = [
    path('list', home, name='book-list'),
    path('read', read),
    path('', index),
    path('create',create_book, name='create-book'),
    path('save', save_book, name='save-book'),
    path('edit/<book_id>', edit_book, name='edit-book'),
    path('save_edit/<book_id>', save_edit_book, name='save-edit-book'),
    path('delete/<book_id>', delete_book, name='delete-book'),
    path('bulk_delete', bulk_delete_books, name='bulk-delete-books'),
    path('categories', CategoryList.as_view(), name='category-list')

]