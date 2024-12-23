from django.urls import path
from .views import CategoryAPIView, CategoryListAPIView, ManufacturerListAPIView, ManufacturerAPIView

urlpatterns = [
    path('categories', CategoryListAPIView.as_view(), name='get_categories'),
    path('category/<int:id>', CategoryAPIView.as_view(), name='categories'),
    path('category', CategoryAPIView.as_view(), name='add_category'), #For post request
    path('manufacturers', ManufacturerListAPIView.as_view(), name='get_manufacturers'),
    path('manufacturer', ManufacturerAPIView.as_view(), name='add_manufacturer'),
    path('manufacturer/<int:id>', ManufacturerAPIView.as_view(), name='add_manufacturer'), #For post request

]

