from django.shortcuts import render
from django.http import HttpResponseRedirect
from ReservasAPP.forms import ReservasForm
from ReservasAPP.models import *
from django.shortcuts import reverse


# Create your views here.


def index(request):
    return render(request, 'index.html')




#vista de las reservas
def reservas(request):
    reservas = Reservas.objects.all()
    return render(request, 'reservas.html', {'Reservas': reservas})

#agregar una reserva
def agregarReserva(request):
    form = ReservasForm()

    if request.method == 'POST':
        form = ReservasForm(request.POST)
        if form.is_valid():
            Reservas.objects.create(
                nombre=form.cleaned_data['nombre'],
                telefono=form.cleaned_data['telefono'],
                fecha=form.cleaned_data['fecha'],  # Asegúrate de que 'fecha' se obtiene aquí
                hora=form.cleaned_data['hora'],
                cantidadPersonas=form.cleaned_data['cantidadPersonas'],
                estadoReserva=form.cleaned_data['estadoReserva']
            )
            return HttpResponseRedirect(reverse('index'))
    
    data = {'form': form}
    return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('reservas'))

def editarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    if request.method == 'POST':
        form = ReservasForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reservas'))
    else:
        form = ReservasForm(instance=reserva)
    data = {'form': form}
    return render(request, 'editarReserva.html', data)
