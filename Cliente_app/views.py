from django.shortcuts import render, redirect
from .models import Cliente

# Vista para mostrar todos los clientes
def inicio_vistaCliente(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"misclientes": losclientes})

# Vista para registrar un nuevo cliente
def registrarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    correo_electronico = request.POST["txtcorreo_electronico"]
    telefono = request.POST["txttelefono"]
    tipo_cliente = request.POST["txttipo_cliente"]
    metodo_de_pago = request.POST["txtmetodo_de_pago"]
    id_producto = request.POST["txtid_producto"]

    guardarcliente = Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        direccion=direccion,
        correo_electronico=correo_electronico,
        telefono=telefono,
        tipo_cliente=tipo_cliente,
        metodo_de_pago=metodo_de_pago,
        id_producto=id_producto
    )  # Guarda el registro

    return redirect("inicio_vistaCliente")

# Vista para seleccionar un cliente y editarlo
def seleccionarCliente(request, id_cliente):
    losclientes = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"misclientes": losclientes})

# Vista para actualizar la información de un cliente
def editarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    correo_electronico = request.POST["txtcorreo_electronico"]
    telefono = request.POST["txttelefono"]
    tipo_cliente = request.POST["txttipo_cliente"]
    metodo_de_pago = request.POST["txtmetodo_de_pago"]
    id_producto = request.POST["txtid_producto"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.correo_electronico = correo_electronico
    cliente.telefono = telefono
    cliente.tipo_cliente = tipo_cliente
    cliente.metodo_de_pago = metodo_de_pago
    cliente.id_producto = id_producto
    cliente.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaCliente")

# Vista para borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()  # Borra el registro
    return redirect("inicio_vistaCliente")
