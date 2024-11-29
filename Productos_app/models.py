from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)  # Para que sean números
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    stock = models.IntegerField()
    fecha_produccion = models.DateField()
    lote = models.CharField(max_length=100)
    id_proveedor = models.IntegerField()
    id_empleado = models.IntegerField()

    def __str__(self):
        return self.nombre
