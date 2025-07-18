from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
#Inicio de sesion requerido
from django.contrib.auth.decorators import login_required
from .models import Perro
#CERRAR SESION
from django.contrib.auth import logout

from rest_framework import viewsets, permissions, status
from .models import Perro, SolicitudAdopcion, CentroAdopcion, Favorito
from .serializers import PerroSerializer, SolicitudAdopcionSerializer, CentroAdopcionSerializer, FavoritoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

import logging
logger = logging.getLogger('api')

# -----------------------------
# ✅ Registro de usuario
# -----------------------------
from django.contrib.auth import get_user_model

def registro_view(request):
    User = get_user_model()  # 👈 usa tu modelo personalizado
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ese nombre de usuario ya existe')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('login')
    return render(request, 'adopcion_perros/registro.html')


# -----------------------------
#  Inicio de sesión
# -----------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # 👈 Asegúrate que 'index' exista en urls.py
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'adopcion_perros/login.html')

# -----------------------------
# Vista principal del sitio
# -----------------------------
def index_view(request):
    return render(request, 'adopcion_perros/index.html')

# -----------------------------
# Otras vistas estáticas
# -----------------------------
def noticias_view(request):
    return render(request, 'adopcion_perros/noticias.html')

def news_view(request):
    return render(request, 'adopcion_perros/news.html')

def colaborador_view(request):
    return render(request, 'adopcion_perros/colaborador.html')


# -----------------------------
# Vistas API REST
# -----------------------------
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
        data['usuario'] = request.user.id
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

#Formulario
@login_required
def adopcion_formulario_view(request):
    perros = Perro.objects.all()
    return render(request, 'adopcion_perros/adopcion_form.html', {'perros': perros})

#Adopcion de la mascota

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Perro

@login_required(login_url='login')  # 👈 esto es lo nuevo
def adopcion_formulario_view(request):
    perros = Perro.objects.all()
    return render(request, 'adopcion_perros/adopcion_form.html', {'perros': perros})


#Cerrar sesion
def logout_view(request):
    logout(request)
<<<<<<< HEAD
    return redirect('login')
=======
    return redirect('index')

#Lista perros

def catalogo_view(request):
    perros = Perro.objects.all()
    return render(request, 'adopcion_perros/catalogo.html', {'perros': perros})

#fundaciones

def fundaciones_view(request):
    fundaciones = CentroAdopcion.objects.all()
    return render(request, 'adopcion_perros/fundaciones.html', {'fundaciones': fundaciones})
>>>>>>> 28d4efba44b37def7ed8644bb51b5d09682c9fca
