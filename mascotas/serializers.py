from rest_framework import serializers
from .models import Mascota


class MascotaSerializer(serializers.ModelSerializer):
    # Convierte Mascota <-> JSON y valida los datos recibidos
    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'especie', 'raza', 'edad', 'peso',
                  'nombre_dueno', 'telefono_dueno', 'observaciones', 'fecha_ingreso']
        read_only_fields = ['id', 'fecha_ingreso']
