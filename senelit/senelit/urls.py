from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Importa redirect para redireccionar la raíz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favorites/', include('myapp.urls')),  # Incluye las rutas de myapp
    path('', lambda request: redirect('favorite_list')),  # Redirige '/' a '/favorites/'
]
