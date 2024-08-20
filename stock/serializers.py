from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' #= ['id', 'name', 'description', 'created_at', 'stock', 'category']
        read_only_fields = ('created_at',) #esto es para que el campo created no se pueda modificar


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' #= ['id', 'name', 'description']