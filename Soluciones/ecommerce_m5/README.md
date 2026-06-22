# Módulo 5 — Base de Datos del Ecommerce

Base de datos relacional de una tienda en línea: usuarios, productos,
categorías, stock, pedidos y detalle de pedidos. Pensada para **PostgreSQL**
(usa `SERIAL`, `ILIKE`, `RETURNING`); es fácilmente adaptable a MySQL o SQLite.

## Archivos y orden de ejecución

| Orden | Archivo | Contenido |
|-------|---------|-----------|
| 1 | `schema.sql` | Definición de tablas, claves y restricciones (DDL) |
| 2 | `seed.sql` | Datos de ejemplo (3 categorías, 10 productos, 5 usuarios, stock, 3 pedidos) |
| 3 | `queries.sql` | Consultas típicas del e-commerce |
| 4 | `transaction.sql` | Operación de compra transaccional |

```bash
# Ejemplo con PostgreSQL
createdb ecommerce
psql -d ecommerce -f schema.sql
psql -d ecommerce -f seed.sql
psql -d ecommerce -f queries.sql
psql -d ecommerce -f transaction.sql
```

También está el modelo entidad-relación en `modelo_er.md` (exportable a
`modelo_er.png`).

## Modelo de datos

- `categorias` 1—N `productos`
- `productos` 1—1 `stock`
- `usuarios` 1—N `pedidos` (campo `rol`: `cliente` / `admin`)
- `pedidos` N—M `productos` a través de `detalle_pedidos`

## Consultas incluidas (queries.sql)

1. Listar productos junto a su categoría.
2. Buscar productos por nombre.
3. Filtrar productos por categoría.
4. Mostrar los productos de un pedido.
5. Calcular el total de un pedido.
6. Identificar productos con stock bajo.

## Operación transaccional (transaction.sql)

Registra una compra completa (crear pedido + detalle + descontar stock)
dentro de un bloque `BEGIN … COMMIT`, de modo que la operación sea atómica:
si algo falla, un `ROLLBACK` deja la base sin cambios.

## Evidencia de ejecución (ejemplo)

```
-- Total del pedido 1
 pedido_id |  total
-----------+---------
         1 | 529970
```

> El esquema y las consultas fueron validados ejecutándolos sobre SQLite
> (versión adaptada de tipos), confirmando que las relaciones y los totales
> son correctos.
