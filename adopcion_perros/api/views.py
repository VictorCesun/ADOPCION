from rest_framework import viewsets, permissions, status
from .models import Perro, SolicitudAdopcion, CentroAdopcion, Favorito
from .serializers import PerroSerializer, SolicitudAdopcionSerializer, CentroAdopcionSerializer, FavoritoSerializer
from rest_framework.permissions import IsAuthenticated
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
logger = logging.getLogger('api')


class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer
    permission_classes = [IsAuthenticated]

class CentroAdopcionViewSet(viewsets.ModelViewSet):
    queryset = CentroAdopcion.objects.all()
    serializer_class = CentroAdopcionSerializer

class SolicitudAdopcionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        solicitudes = SolicitudAdopcion.objects.filter(usuario=request.user)
        serializer = SolicitudAdopcionSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['usuario'] = request.user.id  # Asegura que el usuario autenticado sea el dueño
        serializer = SolicitudAdopcionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolicitudAdopcionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudAdopcion.objects.all()
    serializer_class = SolicitudAdopcionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class FavoritoViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
