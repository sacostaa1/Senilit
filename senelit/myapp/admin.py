
# Register your models here.
from django.contrib import admin
from .models import Servicio, Calificacion

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicio', 'usuario', 'estrellas', 'fecha')
    list_filter = ('estrellas', 'fecha')
    search_fields = ('usuario__username', 'servicio__nombre')
