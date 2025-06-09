from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Define las opciones para el campo JERARQUIA
JERARQUIA_CHOICES = [
    ('CAPITAN', 'Capitán'),
    ('TENIENTE', 'Teniente'),
    ('SUBTENIENTE', 'Subteniente'),
    ('BOMBERO_SUPERIOR', 'Bombero Superior'),
    ('BOMBERO_CALIFICADO', 'Bombero Calificado'),
]

# Define las opciones para el campo ESPECIALIDAD
ESPECIALIDAD_CHOICES = [
    ('CHOFER_LIVIANA', 'Chofer Liviana'),
    ('CHOFER_PESADA', 'Chofer Pesada'),
    ('BUZO_DE_BORDA', 'Buzo de Borda'),
    ('BUZO_DEPORTIVO', 'Buzo Deportivo'),
    ('CONDUCTOR_NAUTICO', 'Conductor Náutico'),
    ('TIMONEL', 'Timonel'),
    ('ELECTRICISTA', 'Electricista'),
    ('FURRIEL', 'Furriel'),
    ('NADADOR_DE_RESCATE', 'Nadador de Rescate'),
    ('GUARDAVIDA', 'Guardavida'),
]


class Task(models.Model):

    apellido_y_nombre = models.CharField(max_length=200)
    jerarquia = models.CharField(
        max_length=100,
        choices=JERARQUIA_CHOICES,
        verbose_name='Jerarquía'
    )
    legajo = models.PositiveIntegerField(unique=True)
    especialidad = MultiSelectField(
        choices=ESPECIALIDAD_CHOICES,
        max_length=200,
        verbose_name='Especialidades del Personal',
        blank=True, 
        null=True 
    )
    importante = models.BooleanField(default=False)
    turno = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return f"{self.apellido_y_nombre} - {self.get_jerarquia_display()} - {self.get_especialidad_display()} - del {self.turno}"