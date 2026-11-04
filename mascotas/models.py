from decimal import Decimal
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


class Mascota(models.Model):
    ESPECIES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Conejo', 'Conejo'),
        ('Otro', 'Otro'),
    ]

    # Los validators se aplican tanto en el formulario web como en la API REST
    nombre = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, 'El nombre debe tener al menos 2 letras.')])
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raza = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(
        help_text='Edad en años',
        validators=[MaxValueValidator(40, 'La edad debe estar entre 0 y 40 años.')])
    peso = models.DecimalField(
        max_digits=5, decimal_places=2, help_text='Peso en kilos',
        validators=[MinValueValidator(Decimal('0.01'), 'El peso debe ser mayor que cero.'),
                    MaxValueValidator(Decimal('150'), 'El peso no puede superar los 150 kg.')])
    nombre_dueno = models.CharField(max_length=100)
    telefono_dueno = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{8,12}$', 'El teléfono debe tener solo números (entre 8 y 12 dígitos).')])
    observaciones = models.TextField(blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
