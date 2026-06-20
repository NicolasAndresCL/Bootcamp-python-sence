from django.contrib import admin

from .models import Producto


# Registramos Producto para poder cargar el catálogo desde /admin.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre",)
