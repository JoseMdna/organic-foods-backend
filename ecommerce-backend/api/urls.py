from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, RecipeList, RecipeDetail
from .auth_views import RegisterView, LoginView, LogoutView, UserInfoView

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/user/', UserInfoView.as_view(), name='user-info'),
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]