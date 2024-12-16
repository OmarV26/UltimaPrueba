from django.shortcuts import render
from django.http import HttpResponseRedirect
from ReservasAPP.forms import ReservasForm
from ReservasAPP.models import *
from django.shortcuts import reverse
from django.http import JsonResponse

#Importaciones para la API
from  ReservasAPP.serializers import ReservasSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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
            return HttpResponseRedirect(reverse('reservas'))
    
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

#Crea una API para la reserva

@api_view(['GET', 'POST'])
def reservas_list(request):
    if request.method == 'GET':
        reservas = Reservas.objects.all()
        serializer = ReservasSerializer(reservas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReservasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
    
@api_view(['GET', 'PUT', 'DELETE'])
def reservas_detail(request, pk):
    try:
        reserva = Reservas.objects.get(pk=pk)
    except Reservas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservasSerializer(reserva)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ReservasSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)