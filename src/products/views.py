from rest_framework.views import APIView
from rest_framework import status, permissions, authentication
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, ManufacturerSerializer
from .models import Category, Product, Manufacturer
from django.http import Http404
# Create your views here.

class CategoryListAPIView(APIView):

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryAPIView(APIView):

    permission_classes = []
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

    def get(self, request, id, format=None):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist as err:
            return Response({'error': str(err)}, status=status.HTTP_404_NOT_FOUND)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data, status=status.HTTP_200_OK)    
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist as error:
            return Response({"error": str(error)}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManufacturerListAPIView(APIView):

    def get(self, request, format=None):
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ManufacturerAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            manufacturer = Manufacturer.objects.get(id=id)
        except Manufacturer.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        try:
            manfacturer = Manufacturer.objects.get(id=id)
        except Manufacturer.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        serializer = ManufacturerSerializer(manfacturer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            manufacturer = Manufacturer.objects.get(id=id)
        except Manufacturer.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProductListAPIView(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCategoryListAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = ProductSerializer(category.product_set.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

class ProductManufacturerListAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            manfacturer = Manufacturer.objects.get(id=id)
        except Manufacturer.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = ProductSerializer(manfacturer.product_set.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ProductAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist as error:
            return Response({"error":str(product)}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist as error:
            return Response({"error":str(error)}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)