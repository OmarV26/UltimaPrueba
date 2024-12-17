from django import forms
from ReservasAPP.models import Reservas
from django.core.exceptions import ValidationError




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

    def cleanCantidadPersonas(self):
        cantidad = self.cleaned_data.get('cantidadPersonas')
        if cantidad > 15:
            raise ValidationError("La cantidad máxima de personas es de 15")
        if cantidad < 1:
            raise ValidationError("Debe haber al menos una persona reservada")
        return cantidad


#de este link encontramos información sobre los validadores de formularios https://www.youtube.com/watch?v=4xrAxCS7vR0
#Aquí tambien leimos un poco mas de información al respecto de metodo clean y el validationError https://www.toolify.ai/es/ai-news-es/aprende-a-validar-formularios-en-django-tutorial-585907#google_vignette
