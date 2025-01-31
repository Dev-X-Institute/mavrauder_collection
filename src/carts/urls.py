from django.urls import path, include
from .views import CartAPIView, CartItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart/item', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('details', CartAPIView.as_view(), name='get_cart'),
    path('', include(router.urls))
] 
