from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.IntegerField(primary_key=True)
    curp=models.CharField(max_length=100)
    telefono= models.IntegerField()
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    email= models.EmailField(max_length=254)
    


    def __str__(self):
        return self.nombre