from django import template
from myapp.models import Favorite  # Ajusta el import a tu caso

register = template.Library()

@register.filter
def is_favorite(service, user):
    # Ajusta la lógica a tu modelo de favoritos
    if user.is_authenticated:
        return Favorite.objects.filter(service=service).exists()
    return False
