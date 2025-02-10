# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio, Calificacion
from django.contrib.auth.decorators import login_required


"""
views.py - Contiene las vistas del sistema, encargadas de manejar la lógica de las páginas.
"""

@login_required
def calificar_servicio(request, servicio_id):
    """
        Vista para calificar un servicio específico.

        Parámetros:
            - request: Objeto HTTP que contiene la petición.
            - servicio_id (int): ID del servicio a calificar.

        Lógica:
            - Si el método es POST, guarda la calificación en la base de datos.
            - Si el método es GET, muestra el formulario para calificar.

        Retorna:
            - Renderiza la plantilla 'calificar.html' con el formulario.
    """


    servicio = get_object_or_404(Servicio, id=servicio_id)


    if request.method == "POST":
        estrellas = request.POST.get("estrellas")
        reseña = request.POST.get("reseña", "")


        calificacion_existente = Calificacion.objects.filter(servicio=servicio, usuario=request.user).first()
        if calificacion_existente:
            calificacion_existente.estrellas = int(estrellas)
            calificacion_existente.reseña = reseña
            calificacion_existente.save()
        else:
            Calificacion.objects.create(
                servicio=servicio,
                usuario=request.user,
                estrellas=int(estrellas),
                reseña=reseña
            )

        return redirect(f"/servicio/{servicio_id}")

    return render(request, "calificar.html", {"servicio": servicio})


def detalle_servicio(request, servicio_id):
    """
        Vista para mostrar los detalles de un servicio y sus calificaciones.

        Parámetros:
            - request: Objeto HTTP con la petición.
            - servicio_id (int): ID del servicio a visualizar.

        Retorna:
            - Renderiza la plantilla 'detalle_servicio.html' con la información del servicio.
    """


    servicio = get_object_or_404(Servicio, id=servicio_id)
    calificaciones = Calificacion.objects.filter(servicio=servicio)

    return render(request, "detalle_servicio.html", {"servicio": servicio, "calificaciones": calificaciones})

def home(request):
    return render(request, "home.html")  # Renderiza un template de inicio
