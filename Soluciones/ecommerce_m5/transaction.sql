-- Ecommerce M5 - transaction.sql
-- Operación transaccional: registrar una compra (PostgreSQL)
-- REQUISITO: antes de ejecutar este archivo deben estar cargados
--            schema.sql y seed.sql (en ese orden).

BEGIN;

WITH nuevo_pedido AS (
    INSERT INTO pedidos (usuario_id, estado)
    VALUES (2, 'pagado')
    RETURNING id
)
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario)
SELECT np.id, p.id, 1, p.precio
FROM nuevo_pedido AS np
CROSS JOIN productos AS p
WHERE p.id = 7;

UPDATE stock
SET cantidad = cantidad - 1
WHERE producto_id = 7;

COMMIT;

