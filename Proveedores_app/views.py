from django.shortcuts import render, redirect
from .models import Proveedor

# Vista para mostrar todos los proveedores
def inicio_vistaProveedor(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"misproveedores": losproveedores})

# Vista para registrar un nuevo proveedor
def registrarProveedor(request):
    id_proveedor = request.POST["txtid_proveedor"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    producto = request.POST["txtproducto"]
    metodo_pago = request.POST["txtmetodo_pago"]
    lote = request.POST["txtlote"]
    id_producto = request.POST["txtid_producto"]

    guardarproveedor = Proveedor.objects.create(
        id_proveedor=id_proveedor,
        nombre=nombre,
        telefono=telefono,
        producto=producto,
        metodo_pago=metodo_pago,
        lote=lote,
        id_producto=id_producto
    )  # Guarda el registro

    return redirect("inicio_vistaProveedor")

# Vista para seleccionar un proveedor y editarlo
def seleccionarProveedor(request, id_proveedor):
    losproveedores = Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedor.html", {"misproveedores": losproveedores})

# Vista para actualizar la información de un proveedor
def editarProveedor(request):
    id_proveedor = request.POST["txtid_proveedor"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    producto = request.POST["txtproducto"]
    metodo_pago = request.POST["txtmetodo_pago"]
    lote = request.POST["txtlote"]
    id_producto = request.POST["txtid_producto"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.producto = producto
    proveedor.metodo_pago = metodo_pago
    proveedor.lote = lote
    proveedor.id_producto = id_producto
    proveedor.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaProveedor")

# Vista para borrar un proveedor
def borrarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()  # Borra el registro
    return redirect("inicio_vistaProveedor")
