from rest_framework import serializers
from .models import Product, Category, Nutrition

class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_by']

class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ['calories', 'protein', 'carbs', 'fat', 'fiber']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    nutrition = NutritionSerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'availability', 
                 'category', 'category_id', 'image_url', 'created_by',
                 'organic', 'vegan', 'glutenFree', 'local', 'nutrition', 'sourcing']
    
    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        nutrition_data = validated_data.pop('nutrition', None)
        category = Category.objects.get(id=category_id)
        nutrition = None
        if nutrition_data:
            nutrition = Nutrition.objects.create(**nutrition_data)
        product = Product.objects.create(
            category=category,
            nutrition=nutrition,
            **validated_data
        )
        return product
    
    def update(self, instance, validated_data):
        nutrition_data = validated_data.pop('nutrition', None)
        if nutrition_data:
            if instance.nutrition:
                nutrition_serializer = NutritionSerializer(instance.nutrition, data=nutrition_data, partial=True)
                if nutrition_serializer.is_valid():
                    nutrition_serializer.save()
            else:
                nutrition = Nutrition.objects.create(**nutrition_data)
                instance.nutrition = nutrition
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance