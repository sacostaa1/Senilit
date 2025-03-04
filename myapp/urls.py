from django.urls import path
from .views import home, detalle_categoria

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>/', detalle_categoria, name='detalle_categoria'),
]
