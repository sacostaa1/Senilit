from django.db import models

# Create your models here.

from django.db import models
import csv
import os
from django.conf import settings


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.ImageField(upload_to='iconos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


    @staticmethod
    def get_all():
        categorias = []
        file_path = os.path.join(settings.BASE_DIR, 'data/categorias.csv')
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                categorias.append(Categoria(row['id'], row['nombre'], row['icono']))
        return categorias


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


    @staticmethod
    def get_by_categoria(categoria_id):
        servicios = []
        with open("data/servicios.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)  # Usa DictReader para evitar errores de índices
            for row in reader:
                if row["categoria_id"] == str(categoria_id):  # Asegurar que la comparación es entre strings
                    servicios.append({
                        "id": row["id"],
                        "nombre": row["nombre"],
                        "descripcion": row["descripcion"],
                        "categoria_id": row["categoria_id"]
                    })
        return servicios

