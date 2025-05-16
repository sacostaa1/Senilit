
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from myapp.views import signup_view

urlpatterns = [
    path('service/create/', views.create_service, name='create_service'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/', views.service_list, name='service_list'),
    path('toggle-favorite/<int:service_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
