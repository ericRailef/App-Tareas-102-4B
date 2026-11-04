from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .api import MascotaViewSet

# El router crea las rutas /api/mascotas/ y /api/mascotas/<id>/
router = DefaultRouter()
router.register('mascotas', MascotaViewSet, basename='api_mascota')

urlpatterns = [
    # Aplicación web
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/<int:id>/', views.detalle_mascota, name='detalle_mascota'),
    path('mascotas/<int:id>/editar/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/<int:id>/eliminar/', views.eliminar_mascota, name='eliminar_mascota'),

    # API REST
    path('api/login/', obtain_auth_token, name='api_login'),   # entrega el token
    path('api/', include(router.urls)),
]
