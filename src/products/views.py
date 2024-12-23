from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, ManufacturerSerializer
from .models import Category, Product, Manufacturer
from django.http import Http404
# Create your views here.

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)
    return Response(categories_serializer.data, status=status.HTTP_200_OK)


class CategoryAPIView(APIView):

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
