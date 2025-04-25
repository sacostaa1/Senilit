from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    available_hours = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(default=0)  # Calificación promedio

    def __str__(self):
        return self.name

    def get_average_rating(self):
        ratings = self.ratings.all()  # Asumimos que hay una relación con el modelo de Ratings
        if ratings:
            return sum([r.rating for r in ratings]) / len(ratings)
        return 0

class Rating(models.Model):
    service = models.ForeignKey(Service, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Calificaciones entre 1 y 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.rating} for {self.service.name}"

class Favorite(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorito - {self.service.name}"
