from django import forms
from ReservasAPP.models import Reservas




class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['nombre', 'telefono', 'fecha', 'hora', 'cantidadPersonas', 'estadoReserva']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'cantidadPersonas': forms.NumberInput(attrs={'class': 'form-control'}),
            'estadoReserva': forms.Select(attrs={'class': 'form-select'}),
        }
