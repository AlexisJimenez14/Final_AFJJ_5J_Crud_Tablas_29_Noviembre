from django.urls import path
from . import views

urlpatterns = [
    path("inicio_vistaProductos", views.inicio_vistaProductos, name="inicio_vistaProductos"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    path("seleccionarProducto/<id_producto>", views.seleccionarProducto, name="seleccionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto"),
    path("borrarProducto/<id_producto>", views.borrarProducto, name="borrarProducto"),
]
