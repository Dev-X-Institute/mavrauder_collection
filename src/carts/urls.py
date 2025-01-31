from django.urls import path
from .views import CartAPIView, CartItemViewSet

urlpatterns = [
    path('cart', CartAPIView.as_view(), name='get_cart'),
    path('cart-item', CartItemViewSet.as_view({
        'get':'list',
        'post':'create',
    }), name='add_cart_item'),
    path('cart-item/<int:id>', CartItemViewSet.as_view({'delete':'destroy'}), name='remove_cart_item'),
]
