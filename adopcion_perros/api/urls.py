from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    adopcion_formulario_view,
    SolicitudAdopcionView,
    PerroViewSet,
    CentroAdopcionViewSet,
    SolicitudAdopcionViewSet,
    FavoritoViewSet,
    login_view,
    logout_view,  # 👈 Importación corregida
    index_view,
    registro_view,
    noticias_view,
    news_view,
    colaborador_view,
)

# API
router = DefaultRouter()
router.register(r'perros', PerroViewSet, basename='perros')
router.register(r'centros', CentroAdopcionViewSet, basename='centros')
router.register(r'adopciones', SolicitudAdopcionViewSet, basename='adopciones')
router.register(r'favoritos', FavoritoViewSet, basename='favoritos')
router.register(r'solicitudes', SolicitudAdopcionViewSet, basename='solicitudes')

# HTML + API
urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # 👈 Ruta de cerrar sesión
    path('registro/', registro_view, name='registro'),
    path('noticias/', noticias_view, name='noticias'),
    path('news/', news_view, name='news'),
    path('colaborador/', colaborador_view, name='colaborador'),
    path('adoptar/', adopcion_formulario_view, name='adoptar'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('fundaciones/', views.fundaciones_view, name='fundaciones'),
]

# Añade las rutas de los ViewSets del router
urlpatterns += router.urls
