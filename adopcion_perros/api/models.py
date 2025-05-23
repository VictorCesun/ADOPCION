from django.db import models
from django.contrib.auth.models import User

class CentroAdopcion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    horario = models.CharField(max_length=100)
    ubicacion_mapa = models.URLField()

    def __str__(self):
        return self.nombre

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    tamano = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    descripcion = models.TextField()
    foto_url = models.URLField()
    disponible = models.BooleanField(default=True)
    centro = models.ForeignKey(CentroAdopcion, on_delete=models.CASCADE, related_name='perros')
    
    # NUEVO CAMPO:
    estado_salud = models.CharField(max_length=100, default='Desconocido')

    def __str__(self):
        return self.nombre


class SolicitudAdopcion(models.Model):
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    mensaje = models.TextField()
    estado = models.CharField(max_length=20, default="Pendiente")
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.perro.nombre}"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'perro')  # evita duplicados

    def __str__(self):
        return f"{self.usuario.username} ♥ {self.perro.nombre}"
