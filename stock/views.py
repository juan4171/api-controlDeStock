from django.shortcuts import render
from .models import Product, Category
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Product objects """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    
class CategoryViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Category objects """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
