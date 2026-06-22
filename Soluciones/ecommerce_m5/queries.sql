-- Ecommerce M5 - queries.sql
-- Consultas típicas de un e-commerce (ejecutar tras schema + seed)

SELECT p.id, p.nombre, c.nombre AS categoria, p.precio
FROM productos AS p
JOIN categorias AS c ON p.categoria_id = c.id
ORDER BY p.id;

SELECT id, nombre, precio
FROM productos
WHERE nombre ILIKE '%teclado%';

SELECT p.nombre, p.precio
FROM productos AS p
JOIN categorias AS c ON p.categoria_id = c.id
WHERE c.nombre = 'Tecnología';

SELECT d.pedido_id, p.nombre, d.cantidad, d.precio_unitario,
       (d.cantidad * d.precio_unitario) AS subtotal
FROM detalle_pedidos AS d
JOIN productos AS p ON d.producto_id = p.id
WHERE d.pedido_id = 1;

SELECT pedido_id, SUM(cantidad * precio_unitario) AS total
FROM detalle_pedidos
WHERE pedido_id = 1
GROUP BY pedido_id;

SELECT p.nombre, s.cantidad
FROM stock AS s
JOIN productos AS p ON s.producto_id = p.id
WHERE s.cantidad < 5
ORDER BY s.cantidad;
