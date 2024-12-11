from django.contrib import admin
from ReservasAPP.models import *

# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'cantidadPersonas', 'estadoReserva')

admin.site.register(Reservas, ReservasAdmin)