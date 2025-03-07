from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Service, Favorite

# Vista para agregar/eliminar favoritos sin autenticación
def toggle_favorite(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    favorite, created = Favorite.objects.get_or_create(service=service)

    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})

    return JsonResponse({'status': 'added'})

# Vista para listar favoritos sin autenticación
def favorite_list(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites.html', {'favorites': favorites})
