from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path("registro/", views.RegistroView.as_view(), name="registro"),
    path("login/", auth_views.LoginView.as_view(template_name="tienda/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Vista protegida: catálogo de productos (solo visualización).
    path("productos/", views.ProductosView.as_view(), name="productos"),
]
