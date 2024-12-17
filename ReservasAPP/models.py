from django.db import models

# Create your models here.


class Reservas(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidadPersonas = models.IntegerField(max_length=15)
    estadoReserva = models.CharField(
        max_length=100,
        choices=[
            ('Reservado', 'Reservado'),
            ('Completada', 'Completada'),
            ('Anulada', 'Anulada'),
            ('No asisten', 'No asisten'),
        ]
    )
    
    def __str__(self):
        return self.nombre
