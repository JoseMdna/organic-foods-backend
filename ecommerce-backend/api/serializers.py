from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'availability', 
                 'category', 'category_id', 'image_url', 'created_by']