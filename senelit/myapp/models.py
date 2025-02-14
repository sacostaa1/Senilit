from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

"""
models.py - Define los modelos de la base de datos.
"""


class Servicio(models.Model):
    """
        Modelo que representa un servicio en el sistema.
    """

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    """
        Modelo que representa una calificación realizada por un usuario a un servicio.
     """

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)  # Relación con el servicio
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    estrellas = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 a 5 estrellas
    reseña = models.TextField(max_length=240, blank=True, null=True)  # Opcional
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha automática

    def __str__(self):
        return f"{self.usuario.username} - {self.servicio.nombre} - {self.estrellas}⭐"
