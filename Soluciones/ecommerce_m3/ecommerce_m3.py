def crear_catalogo():
    """Retorna el catálogo inicial: una lista de diccionarios (5 productos)."""
    return [
        {"id": 1, "nombre": "Polera", "categoria": "ropa", "precio": 9990},
        {"id": 2, "nombre": "Pantalón", "categoria": "ropa", "precio": 19990},
        {"id": 3, "nombre": "Mouse", "categoria": "tecnología", "precio": 14990},
        {"id": 4, "nombre": "Teclado", "categoria": "tecnología", "precio": 24990},
        {"id": 5, "nombre": "Lámpara", "categoria": "hogar", "precio": 12990},
    ]


def mostrar_menu():
    """Muestra el menú principal en pantalla."""
    print("\nBienvenido/a a tu Ecommerce")
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")


def listar_productos(catalogo):
    """Recorre el catálogo e imprime cada producto."""
    print("\n--- CATÁLOGO ---")
    for producto in catalogo:
        print(f"{producto['id']}) {producto['nombre']} | "
              f"{producto['categoria']} | ${producto['precio']}")


def buscar_producto_por_id(catalogo, id_buscado):
    """Recibe el id y RETORNA el producto, o None si no existe."""
    for producto in catalogo:
        if producto["id"] == id_buscado:
            return producto
    return None


def buscar_productos(catalogo):
    """Busca productos por nombre o categoría según el texto ingresado."""
    texto = input("Ingresa nombre o categoría a buscar: ").lower()
    encontrados = []
    for producto in catalogo:
        if texto in producto["nombre"].lower() or texto in producto["categoria"].lower():
            encontrados.append(producto)

    if encontrados:
        print("\n--- RESULTADOS ---")
        for producto in encontrados:
            print(f"{producto['id']}) {producto['nombre']} | "
                  f"{producto['categoria']} | ${producto['precio']}")
    else:
        print("No se encontraron productos con ese criterio.")


def agregar_al_carrito(catalogo, carrito):
    """Pide id y cantidad, valida y agrega el producto al carrito."""
    id_producto = int(input("Id del producto: "))
    producto = buscar_producto_por_id(catalogo, id_producto)

    if producto is None:
        print("Error: no existe un producto con ese id.")
        return

    cantidad = int(input("Cantidad: "))
    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor que 0.")
        return

    carrito.append({"producto": producto, "cantidad": cantidad})
    print(f"Se agregó {cantidad} x {producto['nombre']} al carrito.")


def calcular_total(carrito):
    """Recibe el carrito y RETORNA el total a pagar (suma de subtotales)."""
    total = 0
    for item in carrito:
        total += item["producto"]["precio"] * item["cantidad"]
    return total


def mostrar_carrito_y_total(carrito):
    """Muestra los ítems del carrito y el total. Avisa si está vacío."""
    if not carrito:
        print("El carrito está vacío.")
        return

    print("\n--- CARRITO ---")
    for item in carrito:
        producto = item["producto"]
        cantidad = item["cantidad"]
        subtotal = producto["precio"] * cantidad
        print(f"{producto['id']}) {producto['nombre']} | "
              f"Cantidad: {cantidad} | Precio: ${producto['precio']} | "
              f"Subtotal: ${subtotal}")
    print(f"TOTAL A PAGAR: ${calcular_total(carrito)}")


def main():
    """Función principal: controla el menú con un ciclo while."""
    catalogo = crear_catalogo()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_productos(catalogo)
        elif opcion == "2":
            buscar_productos(catalogo)
        elif opcion == "3":
            agregar_al_carrito(catalogo, carrito)
        elif opcion == "4":
            mostrar_carrito_y_total(carrito)
        elif opcion == "5":
            carrito.clear()
            print("Carrito vaciado correctamente.")
        elif opcion == "0":
            print("¡Gracias por tu compra! Hasta pronto.")
            break   
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
