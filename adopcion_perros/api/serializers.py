from rest_framework import serializers
from .models import Perro, SolicitudAdopcion, CentroAdopcion, Favorito

class CentroAdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroAdopcion
        fields = '__all__'


class PerroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perro
        fields = '__all__'

class SolicitudAdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAdopcion
        fields = '__all__'
        read_only_fields = ['usuario', 'estado', 'fecha_solicitud']

    def validate_telefono(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Número de teléfono inválido.")
        return value

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
