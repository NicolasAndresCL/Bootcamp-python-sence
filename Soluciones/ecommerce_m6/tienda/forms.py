from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Formulario de registro basado en el incorporado de Django.
# Se puede ampliar agregando el correo, por ejemplo.
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
