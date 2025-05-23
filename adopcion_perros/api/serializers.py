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

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
