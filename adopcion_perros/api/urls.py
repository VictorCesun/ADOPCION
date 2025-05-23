from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerroViewSet, CentroAdopcionViewSet, SolicitudAdopcionViewSet, FavoritoViewSet

router = DefaultRouter()
router.register(r'perros', PerroViewSet, basename='perros')
router.register(r'centros', CentroAdopcionViewSet, basename='centros')
router.register(r'adopciones', SolicitudAdopcionViewSet, basename='adopciones')
router.register(r'favoritos', FavoritoViewSet, basename='favoritos')

urlpatterns = [
    path('', include(router.urls)),
]
