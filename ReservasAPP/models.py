from django.db import models

# Create your models here.


class Reservas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidadPersonas = models.IntegerField()
    estadoReserva = models.CharField(
        max_length=100,
        choices=[
            ('Reservado', 'Reservado'),
            ('Completada', 'Completada'),
            ('Anulada', 'Anulada'),
            ('No asisten', 'No asisten'),
        ]
    )
