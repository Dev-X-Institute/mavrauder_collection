from django.urls import path
from .views import (CategoryAPIView, 
                    CategoryListAPIView, 
                    ManufacturerListAPIView, 
                    ManufacturerAPIView, 
                    ProductListAPIView, 
                    ProductCategoryListAPIView, 
                    ProductManufacturerListAPIView, 
                    ProductAPIView)

urlpatterns = [
    path('categories', CategoryListAPIView.as_view(), name='get_categories'),
    path('category/<int:id>', CategoryAPIView.as_view(), name='categories'),
    path('category', CategoryAPIView.as_view(), name='add_category'), #For post request
    path('manufacturers', ManufacturerListAPIView.as_view(), name='get_manufacturers'),
    path('manufacturer', ManufacturerAPIView.as_view(), name='add_manufacturer'), #For post request
    path('manufacturer/<int:id>', ManufacturerAPIView.as_view(), name='add_manufacturer'),
    path('all-products', ProductListAPIView.as_view(), name='get_products'),
    path('category-products/<int:id>', ProductCategoryListAPIView.as_view(), name='get_products_by category'),
    path('manufacturer-products/<int:id>', ProductManufacturerListAPIView.as_view(), name='get_products_by manufacturer'),
    path('prod/<int:id>', ProductAPIView.as_view(), name='get-and-update-product'),
    path('add-product', ProductAPIView.as_view(), name='add-product')
]


