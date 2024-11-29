from django.urls import path
from . import views

urlpatterns = [
    path("inicio_vistaCliente", views.inicio_vistaCliente, name="inicio_vistaCliente"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<id_cliente>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<id_cliente>", views.borrarCliente, name="borrarCliente"),
]
