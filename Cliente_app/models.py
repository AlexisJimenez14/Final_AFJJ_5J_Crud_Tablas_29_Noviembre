from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    tipo_cliente = models.CharField(max_length=100)
    metodo_de_pago = models.CharField(max_length=100)
    id_producto = models.IntegerField()

    def __str__(self):
        return self.nombre
