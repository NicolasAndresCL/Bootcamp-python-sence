// ============================================================
// carrito.js  -  Muestra el carrito y el total a pagar
// ============================================================

const contenedorCarrito = document.querySelector("#contenido-carrito");

function renderizarCarrito() {
  const carrito = obtenerCarrito();

  // Caso 1: el carrito está vacío.
  if (carrito.length === 0) {
    contenedorCarrito.innerHTML = `
      <div class="text-center py-5">
        <p class="lead">Tu carrito está vacío.</p>
        <a href="index.html" class="btn btn-primary">Ver productos</a>
      </div>`;
    return;
  }

  // Caso 2: hay productos. Construimos la tabla y calculamos el total.
  let total = 0;
  let filas = "";

  for (const item of carrito) {
    const producto = buscarProducto(item.id);
    const subtotal = producto.precio * item.cantidad;
    total += subtotal;

    filas += `
      <tr>
        <td>${producto.nombre}</td>
        <td class="text-center">${item.cantidad}</td>
        <td class="text-end">${formatearPrecio(producto.precio)}</td>
        <td class="text-end">${formatearPrecio(subtotal)}</td>
        <td class="text-end">
          <button class="btn btn-sm btn-outline-danger" data-id="${producto.id}">Quitar</button>
        </td>
      </tr>`;
  }

  contenedorCarrito.innerHTML = `
    <div class="table-responsive">
      <table class="table align-middle">
        <thead>
          <tr>
            <th>Producto</th>
            <th class="text-center">Cantidad</th>
            <th class="text-end">Precio</th>
            <th class="text-end">Subtotal</th>
            <th></th>
          </tr>
        </thead>
        <tbody>${filas}</tbody>
        <tfoot>
          <tr>
            <th colspan="3" class="text-end">Total a pagar:</th>
            <th class="text-end text-danger fs-5">${formatearPrecio(total)}</th>
            <th></th>
          </tr>
        </tfoot>
      </table>
    </div>
    <div class="d-flex justify-content-between flex-wrap gap-2">
      <button id="btn-vaciar" class="btn btn-outline-secondary">Vaciar carrito</button>
      <button id="btn-finalizar" class="btn btn-success">Finalizar compra</button>
    </div>`;
}

// Quita un producto del carrito según su id.
function quitarDelCarrito(id) {
  let carrito = obtenerCarrito();
  carrito = carrito.filter((item) => item.id !== id);
  guardarCarrito(carrito);
  actualizarContador();
  renderizarCarrito();
}

// Vacía por completo el carrito.
function vaciarCarrito() {
  localStorage.removeItem("carrito");
  actualizarContador();
  renderizarCarrito();
}

// Simula el cierre de la compra.
function finalizarCompra() {
  alert("¡Gracias por tu compra! (simulación)");
  vaciarCarrito();
}

// Un solo listener maneja los tres tipos de botón (delegación de eventos).
contenedorCarrito.addEventListener("click", function (evento) {
  const objetivo = evento.target;

  if (objetivo.matches("button[data-id]")) {
    quitarDelCarrito(Number(objetivo.dataset.id));
  } else if (objetivo.id === "btn-vaciar") {
    vaciarCarrito();
  } else if (objetivo.id === "btn-finalizar") {
    finalizarCompra();
  }
});

renderizarCarrito();
