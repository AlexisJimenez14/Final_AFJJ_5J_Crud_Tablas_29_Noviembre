from django.db import models

# Create your models here.
class Envio(models.Model):
    id_envio=models.IntegerField(primary_key=True)
    id_producto=models.IntegerField()
    direccion_envio=models.CharField(max_length=100)
    compania_envio= models.CharField(max_length=100)
    fecha_estimada_llegada=models.DateField()
    estado_envio=models.CharField(max_length=100)
    fecha_salida=models.DateField()
    

    def __str__(self):
        return self.estado_envio