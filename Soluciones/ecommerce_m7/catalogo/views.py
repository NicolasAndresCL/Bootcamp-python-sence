from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


# Listar productos (incluye la categoría mediante la relación ORM).
def listar_productos(request):
    productos = Producto.objects.select_related("categoria").all()
    return render(request, "catalogo/listar.html", {"productos": productos})


# Crear un nuevo producto.
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect("listar_productos")
        else:
            messages.error(request, "Revisa los datos del formulario.")
    else:
        form = ProductoForm()
    return render(request, "catalogo/formulario.html",
                  {"form": form, "titulo": "Crear producto"})


# Editar un producto existente (debe existir).
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado correctamente.")
            return redirect("listar_productos")
        else:
            messages.error(request, "Revisa los datos del formulario.")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "catalogo/formulario.html",
                  {"form": form, "titulo": "Editar producto"})


# Eliminar un producto (con confirmación).
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect("listar_productos")
    return render(request, "catalogo/confirmar.html", {"producto": producto})
