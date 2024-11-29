from django.urls import path
from . import views

urlpatterns = [
    path("inicio_vistaEnvio", views.inicio_vistaEnvio, name="inicio_vistaEnvio"),
    path("registrarEnvio/", views.registrarEnvio, name="registrarEnvio"),
    path("seleccionarEnvio/<id_envio>", views.seleccionarEnvio, name="seleccionarEnvio"),
    path("editarEnvio/", views.editarEnvio, name="editarEnvio"),
    path("borrarEnvio/<id_envio>", views.borrarEnvio, name="borrarEnvio"),
]
