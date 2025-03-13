from django.contrib import admin
from django.urls import path, include  # <-- add include clearly here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # ⬅️ ADD THIS LINE CLEARLY
]
