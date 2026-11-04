from rest_framework import viewsets
from .models import Mascota
from .serializers import MascotaSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    # ModelViewSet entrega: GET (lista y por id), POST, PUT/PATCH y DELETE.
    # Por configuración en settings.py exige token (o sesión) para todo.
    queryset = Mascota.objects.all().order_by('id')
    serializer_class = MascotaSerializer
