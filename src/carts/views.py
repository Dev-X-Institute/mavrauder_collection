from rest_framework import generics, viewsets, status, permissions, authentication
from rest_framework.response import Response
from .models import Cart, CartItem 
from .serializers import CartSerializer, CartItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CartAPIView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication, JWTAuthentication]

    def get_object(self):
        if not self.request.user.is_authenticated:
            return Cart.objects.none()
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication, JWTAuthentication]

    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CartItem.objects.none()
        return CartItem.objects.filter(cart__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        
        # Add to cart or update quantity
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.update_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        return Response(self.get_serializer(cart_item).data, 
                        status=status.HTTP_201_CREATED if created else status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Item removed successfully"}, 
                        status=status.HTTP_204_NO_CONTENT)