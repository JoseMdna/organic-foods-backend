from django.contrib import admin
from .models import Category, Product, Nutrition

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('calories', 'protein', 'carbs', 'fat', 'fiber')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'availability', 'category', 'organic', 'vegan', 'created_by')
    list_filter = ('availability', 'category', 'organic', 'vegan', 'glutenFree', 'local')
    search_fields = ('name', 'description', 'sourcing')