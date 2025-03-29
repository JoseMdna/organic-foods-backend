from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class Nutrition(models.Model):
    calories = models.IntegerField(default=0)
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    
    def __str__(self):
        return f"Nutrition: {self.calories} calories"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    organic = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    glutenFree = models.BooleanField(default=False)
    local = models.BooleanField(default=False)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE, null=True, blank=True)
    sourcing = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    dietary = models.JSONField(default=list)
    ingredients = models.JSONField(default=list)
    instructions = models.JSONField(default=list)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title