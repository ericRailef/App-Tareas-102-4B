from django.urls import path
from . import views


urlpatterns = [
    #Ingresar al login
    path('', views.login_pagina, name= 'login_pagina'),

    path('tareas/', views.inicio, name='inicio'),

    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('detalle/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),

    #API LOGIN
    path('api/login/', views.LoginAPIView.as_view(), name='login_api'),

    #API GET Listar Tareas
    path('api/tareas/', views.TareasApiView.as_view(), name='api_tareas'),

    # API DetalleTarea
    path('api/tareas/<int:id>/', views.TareaDetalleApiView.as_view(), name='api_tarea_detalle'),
]