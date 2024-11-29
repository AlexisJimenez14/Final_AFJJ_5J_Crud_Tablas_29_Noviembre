from django.shortcuts import render, redirect
from .models import Envio

# Vista para mostrar todos los envíos
def inicio_vistaEnvio(request):
    losenvios = Envio.objects.all()
    return render(request, "gestionarEnvio.html", {"misenvios": losenvios})

# Vista para registrar un nuevo envío
def registrarEnvio(request):
    id_envio = request.POST["txtid_envio"]
    id_producto = request.POST["txtid_producto"]
    direccion_envio = request.POST["txtdireccion_envio"]
    compania_envio = request.POST["txtcompania_envio"]
    fecha_estimada_llegada = request.POST["txtfecha_estimada_llegada"]
    estado_envio = request.POST["txtestado_envio"]
    fecha_salida = request.POST["txtfecha_salida"]

    guardarenvio = Envio.objects.create(
        id_envio=id_envio,
        id_producto=id_producto,
        direccion_envio=direccion_envio,
        compania_envio=compania_envio,
        fecha_estimada_llegada=fecha_estimada_llegada,
        estado_envio=estado_envio,
        fecha_salida=fecha_salida
    )  # Guarda el registro

    return redirect("inicio_vistaEnvio")

# Vista para seleccionar un envío y editarlo
def seleccionarEnvio(request, id_envio):
    losenvios = Envio.objects.get(id_envio=id_envio)
    fecha_salida = losenvios.fecha_salida.strftime('%Y-%m-%d')  # Formato para mostrar en el input de tipo "date"
    fecha_estimada_llegada = losenvios.fecha_estimada_llegada.strftime('%Y-%m-%d')
    return render(request, "editarEnvio.html", {"misenvios": losenvios,"fecha_salida": fecha_salida, "fecha_estimada_llegada": fecha_estimada_llegada})

# Vista para actualizar la información de un envío
def editarEnvio(request):
    id_envio = request.POST["txtid_envio"]
    id_producto = request.POST["txtid_producto"]
    direccion_envio = request.POST["txtdireccion_envio"]
    compania_envio = request.POST["txtcompania_envio"]
    fecha_estimada_llegada = request.POST["txtfecha_estimada_llegada"]
    estado_envio = request.POST["txtestado_envio"]
    fecha_salida = request.POST["txtfecha_salida"]

    envio = Envio.objects.get(id_envio=id_envio)
    envio.id_producto = id_producto
    envio.direccion_envio = direccion_envio
    envio.compania_envio = compania_envio
    envio.fecha_estimada_llegada = fecha_estimada_llegada
    envio.estado_envio = estado_envio
    envio.fecha_salida = fecha_salida
    envio.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaEnvio")

# Vista para borrar un envío
def borrarEnvio(request, id_envio):
    envio = Envio.objects.get(id_envio=id_envio)
    envio.delete()  # Borra el registro
    return redirect("inicio_vistaEnvio")
