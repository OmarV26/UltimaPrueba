from rest_framework import serializers
from ReservasAPP.models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'