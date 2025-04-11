from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Service, Favorite
from .forms import ServiceForm

def create_service(request):
    """
    Vista para la creación de un nuevo servicio.
    Si la petición es POST, se valida el formulario y se crea el servicio.
    """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return redirect('service_detail', service_id=service.id)
    else:
        form = ServiceForm()
    
    return render(request, 'create_service.html', {'form': form})


def service_detail(request, service_id):
    """
    Muestra el detalle completo de un servicio específico.
    """
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})


def service_list(request):
    """
    Lista todos los servicios creados.
    """
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


def toggle_favorite(request, service_id):
    """
    Alterna la marca de favorito sobre un servicio.
    Si ya era favorito, se elimina; de lo contrario, se agrega.
    Responde con JSON.
    """
    service = get_object_or_404(Service, id=service_id)
    favorite, created = Favorite.objects.get_or_create(service=service)
    
    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    
    return JsonResponse({'status': 'added'})


def favorite_list(request):
    """
    Lista los servicios favoritos.
    Si no hay favoritos, crea uno de prueba.
    """
    favorites = Favorite.objects.all()
    
    if not favorites.exists():
        service, _ = Service.objects.get_or_create(
            name="Servicio Quemado",
            defaults={
                'description': "Servicio de prueba para poder eliminarlo después.",
                'available_hours': "24/7",
                'contact': "contacto@ejemplo.com",
                'location': "Virtual"
            }
        )
        Favorite.objects.get_or_create(service=service)
        favorites = Favorite.objects.all()
    
    return render(request, 'favorites.html', {'favorites': favorites})
