from django.contrib import admin

from .models import Categoria, Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre",)


admin.site.register(Categoria)
