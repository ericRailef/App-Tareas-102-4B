from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tareasapp.views import (
    TareaViewSet,
    crear_tarea,
    detalle_tarea,
    editar_tarea,
    eliminar_tarea,
    inicio,
    login_pagina,
    obtain_auth_token_view,
)

router = DefaultRouter()
router.register(r"tareas", TareaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="index"),
    path("inicio/", inicio, name="inicio"),
    path("login/", login_pagina, name="login"),
    path("crear/", crear_tarea, name="crear"),
    path("detalle/<int:id>/", detalle_tarea, name="detalle"),
    path("editar/<int:id>/", editar_tarea, name="editar"),
    path("eliminar/<int:id>/", eliminar_tarea, name="eliminar"),
    path("api-token-auth/", obtain_auth_token_view, name="api_token_auth"),
    path("api/v1/", include(router.urls)),
]