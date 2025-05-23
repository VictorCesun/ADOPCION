from rest_framework import viewsets, permissions
from .models import Perro, SolicitudAdopcion, CentroAdopcion, Favorito
from .serializers import PerroSerializer, SolicitudAdopcionSerializer, CentroAdopcionSerializer, FavoritoSerializer
from rest_framework.permissions import IsAuthenticated

class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer

class CentroAdopcionViewSet(viewsets.ModelViewSet):
    queryset = CentroAdopcion.objects.all()
    serializer_class = CentroAdopcionSerializer

class SolicitudAdopcionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudAdopcion.objects.all()
    serializer_class = SolicitudAdopcionSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
