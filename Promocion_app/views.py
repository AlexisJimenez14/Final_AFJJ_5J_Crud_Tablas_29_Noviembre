from django.shortcuts import render, redirect
from .models import Promocion

# Vista para mostrar todas las promociones
def inicio_vistaPromocion(request):
    laspromociones = Promocion.objects.all()
    return render(request, "gestionarPromocion.html", {"mispromociones": laspromociones})

# Vista para registrar una nueva promoción
def registrarPromocion(request):
    id_promocion = request.POST["txtid_promocion"]
    descripcion = request.POST["txtdescripcion"]
    fecha_inicio = request.POST["txtfecha_inicio"]
    fecha_fin = request.POST["txtfecha_fin"]
    nombre = request.POST["txtnombre"]
    producto_aplicable = request.POST["txtproducto_aplicable"]
    zona_aplicable = request.POST["txtzona_aplicable"]
    id_producto = request.POST["txtid_producto"]

    guardarpromocion = Promocion.objects.create(
        id_promocion=id_promocion,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        nombre=nombre,
        producto_aplicable=producto_aplicable,
        zona_aplicable=zona_aplicable,
        id_producto=id_producto
    )  # Guarda el registro

    return redirect("inicio_vistaPromocion")

# Vista para seleccionar una promoción y editarla
def seleccionarPromocion(request, id_promocion):
    laspromociones = Promocion.objects.get(id_promocion=id_promocion)
    fecha_fin = laspromociones.fecha_fin.strftime('%Y-%m-%d')
    fecha_inicio = laspromociones.fecha_inicio.strftime('%Y-%m-%d')
    return render(request, "editarPromocion.html", {"mispromociones": laspromociones, "fecha_fin": fecha_fin, "fecha_inicio": fecha_inicio})

# Vista para actualizar la información de una promoción
def editarPromocion(request):
    id_promocion = request.POST["txtid_promocion"]
    descripcion = request.POST["txtdescripcion"]
    fecha_inicio = request.POST["txtfecha_inicio"]
    fecha_fin = request.POST["txtfecha_fin"]
    nombre = request.POST["txtnombre"]
    producto_aplicable = request.POST["txtproducto_aplicable"]
    zona_aplicable = request.POST["txtzona_aplicable"]
    id_producto = request.POST["txtid_producto"]

    promocion = Promocion.objects.get(id_promocion=id_promocion)
    promocion.descripcion = descripcion
    promocion.fecha_inicio = fecha_inicio
    promocion.fecha_fin = fecha_fin
    promocion.nombre = nombre
    promocion.producto_aplicable = producto_aplicable
    promocion.zona_aplicable = zona_aplicable
    promocion.id_producto = id_producto
    promocion.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaPromocion")

# Vista para borrar una promoción
def borrarPromocion(request, id_promocion):
    promocion = Promocion.objects.get(id_promocion=id_promocion)
    promocion.delete()  # Borra el registro
    return redirect("inicio_vistaPromocion")
