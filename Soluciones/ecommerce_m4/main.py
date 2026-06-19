"""
Ecommerce CLI con Programación Orientada a Objetos (Módulo 4)
----------------------------------------------------------------
Este archivo contiene una solución completa en un solo .py, diseñada
para evidenciar de forma clara y ordenada los siguientes conceptos:

- Clases y objetos
- Herencia
- Composición
- Manejo de excepciones estándar y personalizadas
- Lectura/escritura de archivos de texto
- Menús por rol: ADMIN y CLIENTE

La estructura fue intencionalmente mantenida en un solo archivo para:
1) facilitar la lectura del portafolio,
2) dejar trazabilidad completa del desarrollo,
3) reducir complejidad de imports/modularización,
4) evidenciar el aprendizaje del módulo.
"""

from datetime import datetime


class ProductoNoEncontradoError(Exception):
    """Se lanza cuando no existe un producto con el id solicitado."""
    pass


class CantidadInvalidaError(Exception):
    """Se lanza cuando la cantidad ingresada es menor o igual a cero."""
    pass


class PrecioInvalidoError(Exception):
    """Se lanza cuando el precio ingresado no es válido."""
    pass



class Producto:
    def __init__(self, id_producto, nombre, categoria, precio):
        self.id_producto = id_producto

        self.nombre = nombre

        self.categoria = categoria

        self.precio = precio

    def __str__(self):
        return f"{self.id_producto} | {self.nombre} | {self.categoria} | ${self.precio:.0f}"



class Catalogo:
    def __init__(self):
        self.productos = []

    def existe_id(self, id_producto):
        """Retorna True si ya existe un producto con ese id."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return True
        return False

    def agregar_producto(self, producto):
        """Agrega un objeto Producto al catálogo, validando que no se repita el id."""
        if self.existe_id(producto.id_producto):
            raise ValueError(f"Ya existe un producto con id {producto.id_producto}.")
        self.productos.append(producto)

    def listar_productos(self):
        """Muestra todos los productos del catálogo."""
        if not self.productos:
            print("\nNo hay productos registrados en el catálogo.")
            return

        print("\n========== CATÁLOGO DE PRODUCTOS ==========")
        for producto in self.productos:
            print(producto)

    def buscar_por_id(self, id_producto):
        """Busca y retorna un producto por id."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto

        raise ProductoNoEncontradoError(f"No existe un producto con id {id_producto}.")

    def buscar_por_nombre_o_categoria(self, texto_busqueda):
        """Busca productos cuyo nombre o categoría contenga el texto indicado."""
        resultados = []
        texto_busqueda = texto_busqueda.lower().strip()

        for producto in self.productos:
            if (
                texto_busqueda in producto.nombre.lower()
                or texto_busqueda in producto.categoria.lower()
            ):
                resultados.append(producto)

        return resultados

    def actualizar_producto(self, id_producto, nuevo_nombre=None, nueva_categoria=None, nuevo_precio=None):
        """
        Actualiza uno o más atributos del producto.
        Solo modifica los campos que efectivamente reciben un valor.
        """
        producto = self.buscar_por_id(id_producto)

        if nuevo_nombre is not None and nuevo_nombre.strip() != "":
            producto.nombre = nuevo_nombre.strip()

        if nueva_categoria is not None and nueva_categoria.strip() != "":
            producto.categoria = nueva_categoria.strip()

        if nuevo_precio is not None:
            if nuevo_precio <= 0:
                raise PrecioInvalidoError("El precio debe ser mayor que 0.")
            producto.precio = nuevo_precio

    def eliminar_producto(self, id_producto):
        """Elimina un producto del catálogo según su id."""
        
        producto = self.buscar_por_id(id_producto)
        self.productos.remove(producto)

    def guardar_catalogo_en_archivo(self, nombre_archivo="catalogo.txt"):
        """
        Guarda el catálogo actual en un archivo de texto.
        Se usa try/except/finally para evidenciar manejo robusto de errores.
        """
        archivo = None
        try:
            archivo = open(nombre_archivo, "w", encoding="utf-8")

            for producto in self.productos:
                linea = f"{producto.id_producto},{producto.nombre},{producto.categoria},{producto.precio}\n"
                archivo.write(linea)

            print(f"\nCatálogo guardado correctamente en '{nombre_archivo}'.")

        except OSError as error:
            print(f"\nError al guardar el catálogo: {error}")

        finally:
            if archivo:
                archivo.close()

    def cargar_datos_iniciales(self):
        """Carga productos base para facilitar la prueba del sistema."""
        self.agregar_producto(Producto(1, "Polera", "Ropa", 10000))
        self.agregar_producto(Producto(2, "Pantalón", "Ropa", 20000))
        self.agregar_producto(Producto(3, "Mouse", "Tecnología", 15000))
        self.agregar_producto(Producto(4, "Teclado", "Tecnología", 25000))
        self.agregar_producto(Producto(5, "Lámpara", "Hogar", 12000))



class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito validando la cantidad."""
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser mayor que 0.")

        for indice, (producto_actual, cantidad_actual) in enumerate(self.items):
            if producto_actual.id_producto == producto.id_producto:
                self.items[indice] = (producto_actual, cantidad_actual + cantidad)
                return

        self.items.append((producto, cantidad))

    def ver_carrito(self):
        """Muestra todos los ítems del carrito, con subtotal y total."""
        if not self.items:
            print("\nEl carrito está vacío.")
            return

        print("\n============== CARRITO DE COMPRAS ==============")
        for producto, cantidad in self.items:
            subtotal = producto.precio * cantidad
            print(
                f"{producto.nombre} | Cantidad: {cantidad} | "
                f"Precio unitario: ${producto.precio:.0f} | Subtotal: ${subtotal:.0f}"
            )

        print(f"TOTAL A PAGAR: ${self.calcular_total():.0f}")

    def calcular_total(self):
        """Calcula la suma total del carrito."""
        total = 0
        for producto, cantidad in self.items:
            total += producto.precio * cantidad
        return total

    def esta_vacio(self):
        """Retorna True si no hay productos en el carrito."""
        return len(self.items) == 0

    def vaciar_carrito(self):
        """Elimina todos los ítems del carrito."""
        self.items.clear()



class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre



class Admin(Usuario):
    def menu_admin(self, catalogo):
        """Despliega el menú del rol ADMIN."""
        while True:
            print("\n================ MENÚ ADMIN ================")
            print("1. Listar productos")
            print("2. Crear producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Guardar catálogo en archivo")
            print("0. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                catalogo.listar_productos()

            elif opcion == "2":
                self.crear_producto(catalogo)

            elif opcion == "3":
                self.actualizar_producto(catalogo)

            elif opcion == "4":
                self.eliminar_producto(catalogo)

            elif opcion == "5":
                catalogo.guardar_catalogo_en_archivo()

            elif opcion == "0":
                print("\nSaliendo del menú ADMIN...")
                break

            else:
                print("\nOpción inválida. Intente nuevamente.")

    def crear_producto(self, catalogo):
        """Solicita datos por teclado y crea un nuevo producto."""
        try:
            print("\n--- CREAR PRODUCTO ---")
            id_producto = int(input("Ingrese id del producto: "))
            nombre = input("Ingrese nombre del producto: ").strip()
            categoria = input("Ingrese categoría del producto: ").strip()
            precio = float(input("Ingrese precio del producto: "))

            if nombre == "":
                raise ValueError("El nombre no puede quedar vacío.")

            if categoria == "":
                raise ValueError("La categoría no puede quedar vacía.")

            if precio <= 0:
                raise PrecioInvalidoError("El precio debe ser mayor que 0.")

            nuevo_producto = Producto(id_producto, nombre, categoria, precio)
            catalogo.agregar_producto(nuevo_producto)
            print("\nProducto agregado correctamente.")

        except ValueError as error:
            print(f"\nError de entrada: {error}")
        except PrecioInvalidoError as error:
            print(f"\nError: {error}")

    def actualizar_producto(self, catalogo):
        """Permite modificar nombre, categoría y/o precio de un producto."""
        try:
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_producto = int(input("Ingrese id del producto a actualizar: "))

            # Se permite presionar Enter para dejar un campo sin cambios.
            nuevo_nombre = input("Nuevo nombre (Enter para omitir): ").strip()
            nueva_categoria = input("Nueva categoría (Enter para omitir): ").strip()
            texto_precio = input("Nuevo precio (Enter para omitir): ").strip()

            nuevo_precio = None
            if texto_precio != "":
                nuevo_precio = float(texto_precio)

            catalogo.actualizar_producto(
                id_producto=id_producto,
                nuevo_nombre=nuevo_nombre if nuevo_nombre != "" else None,
                nueva_categoria=nueva_categoria if nueva_categoria != "" else None,
                nuevo_precio=nuevo_precio,
            )

            print("\nProducto actualizado correctamente.")

        except ProductoNoEncontradoError as error:
            print(f"\nError: {error}")
        except ValueError as error:
            print(f"\nError de entrada: {error}")
        except PrecioInvalidoError as error:
            print(f"\nError: {error}")

    def eliminar_producto(self, catalogo):
        """Elimina un producto del catálogo según su id."""
        try:
            print("\n--- ELIMINAR PRODUCTO ---")
            id_producto = int(input("Ingrese id del producto a eliminar: "))
            catalogo.eliminar_producto(id_producto)
            print("\nProducto eliminado correctamente.")

        except ProductoNoEncontradoError as error:
            print(f"\nError: {error}")
        except ValueError:
            print("\nDebe ingresar un id numérico válido.")



class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)

        self.carrito = Carrito()

    def menu_cliente(self, catalogo):
        """Despliega el menú del rol CLIENTE."""
        while True:
            print("\n================ MENÚ CLIENTE ================")
            print("1. Ver catálogo")
            print("2. Buscar producto por nombre o categoría")
            print("3. Agregar producto al carrito")
            print("4. Ver carrito y total")
            print("5. Confirmar compra")
            print("0. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                catalogo.listar_productos()

            elif opcion == "2":
                self.buscar_productos(catalogo)

            elif opcion == "3":
                self.agregar_al_carrito(catalogo)

            elif opcion == "4":
                self.carrito.ver_carrito()

            elif opcion == "5":
                self.confirmar_compra()

            elif opcion == "0":
                print("\nSaliendo del menú CLIENTE...")
                break

            else:
                print("\nOpción inválida. Intente nuevamente.")

    def buscar_productos(self, catalogo):
        """Permite buscar productos por nombre o categoría."""
        texto = input("Ingrese nombre o categoría a buscar: ").strip()
        resultados = catalogo.buscar_por_nombre_o_categoria(texto)

        if resultados:
            print("\n========== RESULTADOS DE BÚSQUEDA ==========")
            for producto in resultados:
                print(producto)
        else:
            print("\nNo se encontraron productos con ese criterio.")

    def agregar_al_carrito(self, catalogo):
        """Solicita un producto y una cantidad, y los agrega al carrito."""
        try:
            print("\n--- AGREGAR PRODUCTO AL CARRITO ---")
            id_producto = int(input("Ingrese id del producto: "))
            cantidad = int(input("Ingrese cantidad: "))

            producto = catalogo.buscar_por_id(id_producto)
            self.carrito.agregar_producto(producto, cantidad)
            print("\nProducto agregado al carrito correctamente.")

        except ProductoNoEncontradoError as error:
            print(f"\nError: {error}")
        except CantidadInvalidaError as error:
            print(f"\nError: {error}")
        except ValueError:
            print("\nDebe ingresar valores numéricos válidos.")

    def confirmar_compra(self, nombre_archivo="ordenes.txt"):
        """
        Registra la compra en archivo si el carrito no está vacío.
        Luego vacía el carrito.
        """
        if self.carrito.esta_vacio():
            print("\nNo se puede confirmar la compra porque el carrito está vacío.")
            return

        archivo = None
        try:
            archivo = open(nombre_archivo, "a", encoding="utf-8")

            # Encabezado de la orden.
            archivo.write("\n========================================\n")
            archivo.write(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            archivo.write(f"Cliente: {self.nombre}\n")
            archivo.write("Detalle de compra:\n")

            # Se registra cada producto comprado.
            for producto, cantidad in self.carrito.items:
                subtotal = producto.precio * cantidad
                archivo.write(
                    f"- {producto.nombre} | Cantidad: {cantidad} | "
                    f"Precio unitario: {producto.precio:.0f} | Subtotal: {subtotal:.0f}\n"
                )

            archivo.write(f"TOTAL: {self.carrito.calcular_total():.0f}\n")

            print(f"\nCompra registrada correctamente en '{nombre_archivo}'.")

            # Después de registrar la compra, se vacía el carrito.
            self.carrito.vaciar_carrito()
            print("Carrito vaciado correctamente.")

        except OSError as error:
            print(f"\nError al registrar la compra: {error}")

        finally:
            if archivo:
                archivo.close()



class Aplicacion:
    def __init__(self):
        self.catalogo = Catalogo()
        self.catalogo.cargar_datos_iniciales()

    def iniciar(self):
        """Muestra el menú principal y permite seleccionar rol."""
        while True:
            print("\n============================================")
            print("     ECOMMERCE CLI CON POO - MÓDULO 4")
            print("============================================")
            print("1. Ingresar como ADMIN")
            print("2. Ingresar como CLIENTE")
            print("0. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                admin = Admin("Administrador")
                admin.menu_admin(self.catalogo)

            elif opcion == "2":
                nombre_cliente = input("Ingrese nombre del cliente: ").strip()

                if nombre_cliente == "":
                    print("\nEl nombre del cliente no puede quedar vacío.")
                else:
                    cliente = Cliente(nombre_cliente)
                    cliente.menu_cliente(self.catalogo)

            elif opcion == "0":
                print("\nPrograma finalizado.")
                break

            else:
                print("\nOpción inválida. Intente nuevamente.")



if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()
