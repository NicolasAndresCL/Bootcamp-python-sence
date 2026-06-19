# Módulo 4 — E-commerce CLI con POO y roles

Reestructuración del e-commerce de consola del Módulo 3, ahora con
**Programación Orientada a Objetos**, **roles** (ADMIN y CLIENTE),
**manejo de excepciones** y **lectura/escritura de archivos**.

## Cómo ejecutarlo

```
python main.py
```

Al iniciar se elige el rol (ADMIN o CLIENTE) y se muestra su menú.

## Diseño orientado a objetos

| Clase | Responsabilidad | Concepto |
|-------|-----------------|----------|
| `Producto` | Datos de un producto | Clase base de datos |
| `Catalogo` | Administra los productos | Composición (contiene Productos) |
| `Carrito` | Ítems seleccionados + cantidades | Composición |
| `Usuario` | Clase base de usuarios | Herencia (base) |
| `Admin`, `Cliente` | Menús y acciones por rol | Herencia + polimorfismo |
| `Aplicacion` | Coordina menús y flujo | Orquestación |

## Cómo cumple la rúbrica

- **Diseño OO:** herencia (`Admin`/`Cliente` → `Usuario`) y composición
  (`Catalogo` y `Carrito`).
- **Roles y funcionalidades:** ADMIN gestiona el catálogo (crear, actualizar,
  eliminar, listar, guardar en archivo); CLIENTE busca, agrega al carrito,
  ve el total y confirma compra.
- **Excepciones:** excepciones personalizadas (`ProductoNoEncontradoError`,
  `CantidadInvalidaError`, `PrecioInvalidoError`) + estándar, con
  `try/except/finally`.
- **Archivos:** guarda el catálogo (`catalogo.txt`) y registra las compras
  con fecha/hora en `ordenes.txt` (obligatorio).
- **Legibilidad:** `snake_case`, indentación correcta y comentarios.

> Solo usa la librería estándar (`datetime`). Sin bases de datos, frameworks
> ni dependencias externas.
