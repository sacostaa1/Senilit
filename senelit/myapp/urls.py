from django.urls import path
from .views import favorite_list, toggle_favorite

urlpatterns = [
    path('favorites/', favorite_list, name='favorite_list'),
    path('toggle_favorite/<int:service_id>/', toggle_favorite, name='toggle_favorite'),
]
