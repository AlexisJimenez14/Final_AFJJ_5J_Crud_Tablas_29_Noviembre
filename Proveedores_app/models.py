from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    telefono= models.IntegerField()
    producto=models.CharField(max_length=100)
    metodo_pago=models.CharField(max_length=100)
    lote=models.CharField(max_length=100)
    id_producto=models.IntegerField()
    
    def __str__(self):
        return self.nombre