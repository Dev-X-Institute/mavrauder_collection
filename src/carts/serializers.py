from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer

# serializers.py
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']  # Remove nested ProductSerializer

    # Optional: Add product details in the response (not the input)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        return representation


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'created_At', 'updated_At']
        read_only_fields = ['total_price', 'created_At', 'updated_At']

    def get_total_price(self, model):
        return model.total_price()