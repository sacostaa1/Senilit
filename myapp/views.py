from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Servicio


def home(request):
    categorias = Categoria.get_all()
    return render(request, 'home.html', {'categorias': categorias})


def detalle_categoria(request, categoria_id):
    categoria = next((c for c in Categoria.get_all() if c.id == str(categoria_id)), None)
    if not categoria:
        return render(request, '404.html', status=404)

    servicios = Servicio.get_by_categoria(categoria_id)
    return render(request, 'detalle_categoria.html', {'categoria': categoria, 'servicios': servicios})
