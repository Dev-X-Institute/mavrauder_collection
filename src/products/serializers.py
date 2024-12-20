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
    manufacturer = ManufacturerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    manufacturer_id = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all(), source='manufacturer') 
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'manufacturer', 'category', 'manufacturer_id', 'category_id', 'inventory', 'price']
        read_only_fields = ['id']