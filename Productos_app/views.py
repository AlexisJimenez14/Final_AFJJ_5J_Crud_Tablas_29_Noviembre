from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.
def inicio_vistaProductos(request):
    losproductos = Productos.objects.all()
    return render(request, "gestionarProductos.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST["txtid_producto"]
    nombre = request.POST["txtnombre"]
    precio = request.POST["txtprecio"]
    cantidad = request.POST["txtcantidad"]
    stock = request.POST["txtstock"]
    fecha_produccion = request.POST["txtfecha_produccion"]
    lote = request.POST["txtlote"]
    id_proveedor = request.POST["txtid_proveedor"]
    id_empleado = request.POST["txtid_empleado"]

    Productos.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        precio=precio,
        cantidad=cantidad,
        stock=stock,
        fecha_produccion=fecha_produccion,
        lote=lote,
        id_proveedor=id_proveedor,
        id_empleado=id_empleado,
    )

    return redirect("inicio_vistaProductos")

def seleccionarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    fecha_produccion = producto.fecha_produccion.strftime('%Y-%m-%d')
    return render(request, "editarProductos.html", {"misproductos": producto,"fecha_produccion": fecha_produccion})

def editarProducto(request):
    id_producto = request.POST["txtid_producto"]
    nombre = request.POST["txtnombre"]
    precio = request.POST["txtprecio"]
    cantidad = request.POST["txtcantidad"]
    stock = request.POST["txtstock"]
    fecha_produccion = request.POST["txtfecha_produccion"]
    lote = request.POST["txtlote"]
    id_proveedor = request.POST["txtid_proveedor"]
    id_empleado = request.POST["txtid_empleado"]

    producto = Productos.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.precio = precio
    producto.cantidad = cantidad
    producto.stock = stock
    producto.fecha_produccion = fecha_produccion
    producto.lote = lote
    producto.id_proveedor = id_proveedor
    producto.id_empleado = id_empleado
    producto.save()

    return redirect("inicio_vistaProductos")

def borrarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("inicio_vistaProductos")
