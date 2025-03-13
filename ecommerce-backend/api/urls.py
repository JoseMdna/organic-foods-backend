from django.urls import path
from .views import ProductList, ProductDetail, CategoryList

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('categories/', CategoryList.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('products/', views.ProductList.as_view(), name='product-list'),
]
