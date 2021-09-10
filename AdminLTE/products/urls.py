from django.urls import path
from .views import index,home,add_product,save_product,CategoryList,delete_product, bulk_delete_product,edit_product,save_edit_product,add_category,save_category

urlpatterns = [
    path('productlist', home, name='product-list'),
    path('', index, name='dashboard'),
    path('addproduct',add_product, name='add-product'),
    path('saveproduct', save_product, name='save-product'),
    path('addcategory',add_category, name='add-category'),
    path('savecategory',save_category,name='save-category'),
    path('edit/<product_id>', edit_product, name='edit-product'),
    path('save_edit/<product_id>', save_edit_product, name='save-edit-product'),
    path('categories', CategoryList.as_view(), name='category-list'),
    path('delete/<product_id>', delete_product, name='delete-product'),
    path('bulk_delete', bulk_delete_product, name='bulk-delete-products'),



]