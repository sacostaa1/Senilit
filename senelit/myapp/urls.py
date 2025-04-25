
from django.urls import path
from . import views

urlpatterns = [
    path('service/create/', views.create_service, name='create_service'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/', views.service_list, name='service_list'),
    path('toggle-favorite/<int:service_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),
 

]
