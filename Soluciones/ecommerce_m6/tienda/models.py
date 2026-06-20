from django.db import models


# Producto del catálogo de la tienda.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
