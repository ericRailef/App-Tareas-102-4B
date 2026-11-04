from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):
    # Las validaciones (largo, rangos, teléfono) están en models.py,
    # así el formulario y la API usan exactamente las mismas reglas.
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'peso',
                  'nombre_dueno', 'telefono_dueno', 'observaciones']
        labels = {
            'nombre': 'Nombre de la mascota',
            'nombre_dueno': 'Nombre del dueño',
            'telefono_dueno': 'Teléfono del dueño',
            'edad': 'Edad (años)',
            'peso': 'Peso (kg)',
        }
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
