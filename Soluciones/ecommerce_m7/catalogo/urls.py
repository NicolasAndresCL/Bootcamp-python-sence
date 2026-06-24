from django.urls import path

from . import views

# Rutas bajo /products/ (ver core/urls.py).
urlpatterns = [
    path("", views.listar_productos, name="listar_productos"),                # /products/
    path("create/", views.crear_producto, name="crear_producto"),            # /products/create/
    path("edit/<int:id>/", views.editar_producto, name="editar_producto"),   # /products/edit/<id>/
    path("delete/<int:id>/", views.eliminar_producto, name="eliminar_producto"),  # /products/delete/<id>/
]
