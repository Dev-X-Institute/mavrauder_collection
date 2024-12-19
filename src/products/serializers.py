from rest_framework import serializers
from .models import Category, Manufacturer, Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name']
        read_only_fields = ['id']


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['id', 'manufacturer_name', 'email', 'phone_number', 'location']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'manufacturer_id', 'category_id', 'inventory', 'price']
        read_only_fields = ['id', 'manufacturer_id', 'category_id']