from django.urls import path
from .views import CategoryAPIView, get_categories

urlpatterns = [
    path('categories', get_categories, name='get_categories'),
    path('category/<int:id>', CategoryAPIView.as_view(), name='categories'),
    path('category', CategoryAPIView.as_view(), name='add_category'),
]

