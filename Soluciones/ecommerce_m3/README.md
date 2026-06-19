# Módulo 3 — E-commerce CLI (Fundamentos de Python)

Aplicación de consola que simula un ecommerce básico: catálogo de
productos, búsqueda, carrito de compras y cálculo del total.

## Cómo ejecutarlo

```
python ecommerce_m3.py
```

## Menú

```
1) Ver catálogo de productos
2) Buscar producto por nombre o categoría
3) Agregar producto al carrito
4) Ver carrito y total
5) Vaciar carrito
0) Salir
```

El menú se repite hasta elegir `0) Salir`.

## Cómo cumple los requisitos del enunciado

- **Tipos de datos:** `int` (id, precio), `str` (nombre, categoría), uso
  de `bool` en validaciones.
- **Estructuras de datos:** el catálogo es una **lista de diccionarios** y
  el carrito es otra **lista de diccionarios**.
- **Condicionales:** validan la opción del menú, que el id exista y que la
  cantidad sea mayor que 0.
- **Ciclos:** un `while` controla el menú principal y varios `for`
  recorren el catálogo y el carrito.
- **Funciones:** hay más de 3 funciones separadas; `calcular_total(carrito)`
  recibe un parámetro y **retorna un valor**.
- Nombres en **snake_case**, indentación correcta y comentarios breves.
