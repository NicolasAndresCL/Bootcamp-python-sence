# Modelo Entidad-Relación — Ecommerce (Módulo 5)

> Exporta el bloque Mermaid a PNG (https://mermaid.live) y guárdalo como
> `modelo_er.png` para cumplir el entregable de "diagrama ER (imagen)".

```mermaid
erDiagram
    CATEGORIAS   ||--o{ PRODUCTOS       : "clasifica"
    PRODUCTOS    ||--|| STOCK           : "tiene"
    USUARIOS     ||--o{ PEDIDOS         : "realiza"
    PEDIDOS      ||--o{ DETALLE_PEDIDOS : "contiene"
    PRODUCTOS    ||--o{ DETALLE_PEDIDOS : "aparece en"

    CATEGORIAS {
        int id PK
        string nombre
    }
    USUARIOS {
        int id PK
        string nombre
        string email
        string rol
    }
    PRODUCTOS {
        int id PK
        string nombre
        numeric precio
        int categoria_id FK
    }
    STOCK {
        int producto_id PK, FK
        int cantidad
    }
    PEDIDOS {
        int id PK
        int usuario_id FK
        timestamp fecha
        string estado
    }
    DETALLE_PEDIDOS {
        int id PK
        int pedido_id FK
        int producto_id FK
        int cantidad
        numeric precio_unitario
    }
```

## Decisiones de diseño

- **Categorías → Productos:** un producto pertenece a una categoría (1:N).
- **Productos → Stock:** relación 1:1; cada producto tiene un registro de
  stock con su cantidad disponible.
- **Usuarios → Pedidos:** un usuario realiza muchos pedidos (1:N). El campo
  `rol` distingue a clientes de administradores.
- **Pedidos ↔ Productos:** relación N:M resuelta con `detalle_pedidos`, que
  además guarda la `cantidad` y el `precio_unitario` al momento de la compra.
