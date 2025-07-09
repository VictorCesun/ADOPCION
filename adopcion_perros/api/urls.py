from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import adopcion_formulario_view, SolicitudAdopcionView
from . import views
from .views import (
    PerroViewSet,
    CentroAdopcionViewSet,
    SolicitudAdopcionViewSet,
    FavoritoViewSet,
    login_view,
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
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('noticias/', views.noticias_view, name='noticias'),
    path('news/', views.news_view, name='news'),
    path('colaborador/', views.colaborador_view, name='colaborador'),
    path('adoptar/', adopcion_formulario_view, name='adoptar'),
    path('api/adopciones/', SolicitudAdopcionView.as_view(), name='api_adopciones'),
    path('login/', login_view, name='login'),

    # Puedes agregar más vistas aquí
]




urlpatterns += router.urls