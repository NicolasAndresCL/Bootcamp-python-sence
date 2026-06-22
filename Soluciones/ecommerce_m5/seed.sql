-- Ecommerce M5 - seed.sql
-- Datos de ejemplo (ejecutar después de schema.sql)
INSERT INTO categorias (nombre) VALUES
    ('Tecnología'),   -- id 1
    ('Hogar'),        -- id 2
    ('Ropa');         -- id 3

INSERT INTO usuarios (nombre, email, rol) VALUES
    ('Admin General', 'admin@tienda.cl', 'admin'),
    ('Ana Soto', 'ana@mail.cl', 'cliente'),
    ('Luis Rojas', 'luis@mail.cl', 'cliente'),
    ('María Pérez', 'maria@mail.cl', 'cliente'),
    ('Pedro Díaz', 'pedro@mail.cl', 'cliente');

INSERT INTO productos (nombre, precio, categoria_id) VALUES
    ('Notebook 14"', 499990, 1),       -- id 1
    ('Mouse inalámbrico', 14990, 1),   -- id 2
    ('Teclado mecánico', 39990, 1),    -- id 3
    ('Audífonos Bluetooth', 29990, 1), -- id 4
    ('Lámpara de escritorio', 12990, 2),-- id 5
    ('Set de sábanas', 24990, 2),      -- id 6
    ('Cafetera', 44990, 2),            -- id 7
    ('Polera algodón', 9990, 3),       -- id 8
    ('Pantalón jeans', 19990, 3),      -- id 9
    ('Chaqueta cortavientos', 34990, 3);-- id 10

INSERT INTO stock (producto_id, cantidad) VALUES
    (1, 5), (2, 50), (3, 20), (4, 3), (5, 30),
    (6, 15), (7, 8), (8, 100), (9, 40), (10, 2);

INSERT INTO pedidos (usuario_id, estado) VALUES (2, 'pagado');   -- id 1
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) VALUES
    (1, 1, 1, 499990),
    (1, 2, 2, 14990);

INSERT INTO pedidos (usuario_id, estado) VALUES (3, 'pagado');   -- id 2
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) VALUES
    (2, 8, 3, 9990),
    (2, 9, 1, 19990);

INSERT INTO pedidos (usuario_id, estado) VALUES (4, 'pendiente');-- id 3
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) VALUES
    (3, 7, 1, 44990);
