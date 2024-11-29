from django.db import models

# Create your models here.
class Promocion(models.Model):
    id_promocion =models.IntegerField(primary_key=True)
    descripcion = models.TextField()  # Cambié de IntegerField a TextField para una mejor descripción
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    nombre = models.CharField(max_length=100)
    producto_aplicable = models.CharField(max_length=100)
    zona_aplicable = models.CharField(max_length=100)
    id_producto = models.IntegerField()
    

    def __str__(self):
        return self.nombre
