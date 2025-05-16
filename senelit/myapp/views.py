from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Service, Favorite
from .forms import ServiceForm
from .models import Service, Rating
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def mi_vista_privada(request):
    return render(request, 'privado.html')

@login_required
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

@login_required
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
    services = services.order_by('-rating')  # Ordenar por calificación descendente
    return render(request, 'service_list.html', {'services': services})

@login_required
def service_detail(request, service_id):
    """
    Muestra el detalle completo de un servicio específico y permite calificarlo.
    """
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        rating_value = int(request.POST.get('rating', 0))

        # Validar que la calificación esté entre 1 y 5
        if 1 <= rating_value <= 5:
            # Verificar si el usuario ya ha calificado el servicio
            rating, created = Rating.objects.get_or_create(
                service=service,
                defaults={'rating': rating_value}
            )

            # Si ya existe una calificación, actualizarla
            if not created:
                rating.rating = rating_value
                rating.save()

            return redirect('service_detail', service_id=service.id)

    return render(request, 'service_detail.html', {'service': service})



@login_required
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

@login_required
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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente
            return redirect('/')  # o donde quieras redirigir
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
