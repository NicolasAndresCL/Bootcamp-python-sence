from django.db import models


# Categoría a la que pertenece un producto.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# Producto del catálogo. Relación: muchos productos -> una categoría.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,   # no permite borrar una categoría con productos
        related_name="productos",
    )

    def __str__(self):
        return self.nombre
