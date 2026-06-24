# Módulo 7 — Ecommerce: Acceso a Datos con Django (CRUD de catálogo)

> **Repositorio GitHub:** https://github.com/NicolasAndresCL/Bootcamp-python-sence
> Aquí puedes revisar y verificar el proyecto en línea.

Módulo de **administración del catálogo** de un e-commerce: permite listar,
crear, editar y eliminar productos usando el **ORM de Django**, vistas,
templates, el sistema de mensajes y el panel administrativo.

## Motor de base de datos

- Por defecto: **SQLite** (funciona sin configuración, ideal para revisar).
- Para **PostgreSQL** (lo que enseña el módulo): instalar
  `pip install psycopg2-binary` y reemplazar `DATABASES` en `core/settings.py`:
  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "ecommerce",
          "USER": "tu_usuario",
          "PASSWORD": "tu_contraseña",
          "HOST": "localhost",
          "PORT": "5432",
      }
  }
  ```
- Utilizar por protección de datos `pip install python-dotenv` y por supuesto un archivo .env

## Modelo de datos

- **Categoria** (`nombre`).
- **Producto** (`nombre`, `descripcion`, `precio`, `categoria` → FK).
  Relación: muchos productos pertenecen a una categoría.

- Por seguridad se crea un archivo .gitignore para evitar subir bd y variables de entorno.

## Rutas principales (módulo de administración)

| Ruta | Acción |
|------|--------|
| `/products/` | Listado de productos |
| `/products/create/` | Formulario de creación |
| `/products/edit/<id>/` | Formulario de edición |
| `/products/delete/<id>/` | Eliminación (con confirmación) |
| `/admin/` | Panel administrativo de Django (modelo `Producto` registrado) |

## Pasos para ejecutar

```bash
python -m venv env
env\Scripts\activate          

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   
python manage.py runserver
```

Abrir http://127.0.0.1:8000/ (redirige al listado de productos).

## Cómo cumple la rúbrica

- **Modelos y ORM:** `Producto` y `Categoria` definidos en `models.py`.
- **Relaciones y migraciones:** FK `Producto → Categoria`; migraciones con
  `makemigrations` / `migrate`.
- **CRUD de productos:** vistas `listar`, `crear`, `editar`, `eliminar` con el
  ORM y ModelForm.
- **Integración vistas + datos:** los templates muestran y procesan los datos.
- **Validación:** el precio debe ser mayor que 0 (en `ProductoForm.clean_precio`).
- **Mensajes:** feedback de éxito/error con `django.contrib.messages`.
- **Django Admin:** modelo `Producto` registrado con `list_display`, filtros y
  búsqueda.

## Evidencias (capturas sugeridas)

1. Listado de productos en `/products/`.
2. Formulario de creación/edición.
3. Producto gestionado desde `/admin/`.
