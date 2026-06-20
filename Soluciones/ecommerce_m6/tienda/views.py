from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .forms import RegistroForm
from .models import Producto


# Página pública de inicio.
class InicioView(TemplateView):
    template_name = "tienda/inicio.html"


# Registro de usuario: al crear la cuenta, redirige al login.
class RegistroView(CreateView):
    template_name = "tienda/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy("login")


# Vista PROTEGIDA: el catálogo de productos solo se muestra a usuarios
# autenticados. LoginRequiredMixin redirige al login a quien no tenga sesión.
class ProductosView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "tienda/productos.html"
    context_object_name = "productos"
