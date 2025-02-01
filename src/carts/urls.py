from django.urls import path, include
from .views import CartItemViewSet, CartAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart-item', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('details/', CartAPIView.as_view(), name='get_cart'),
    # The router includes all the registered viewsets' URLs
    path('', include(router.urls)),
] 
