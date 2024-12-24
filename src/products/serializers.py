from rest_framework import serializers
from .models import Category, Manufacturer, Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_At', 'updated_At']
        read_only_fields = ['id']


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['id', 'manufacturer_name', 'email', 'phone_number', 'location', 'created_At', 'updated_At']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True, source='manufacturer_id')
    category = CategorySerializer(read_only=True, source='category_id')
    manufacturer_id = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all()) 
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'manufacturer', 'category', 'manufacturer_id', 'category_id', 'inventory', 'price']
        read_only_fields = ['id', 'manufacturer', 'category']
