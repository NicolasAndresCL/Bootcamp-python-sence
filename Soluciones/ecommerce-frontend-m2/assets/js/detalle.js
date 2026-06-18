// ============================================================
// detalle.js  -  Muestra el detalle de un producto
// ============================================================
// El id del producto viaja en la URL, por ejemplo: detalle.html?id=3

const parametros = new URLSearchParams(window.location.search);
const idProducto = Number(parametros.get("id"));
const producto = buscarProducto(idProducto);

const contenedorDetalle = document.querySelector("#detalle-producto");

if (!producto) {
  // Si el id no existe o no vino en la URL, avisamos al usuario.
  contenedorDetalle.innerHTML = `
    <div class="alert alert-warning">
      Producto no encontrado. <a href="index.html">Volver al inicio</a>.
    </div>`;
} else {
  // Cambiamos el título de la pestaña del navegador.
  document.title = `${producto.nombre} | AstroShop`;

  contenedorDetalle.innerHTML = `
    <div class="row g-4 align-items-center">
      <div class="col-12 col-md-6">
        <img src="${producto.imagen}" class="img-fluid rounded shadow-sm" alt="${producto.nombre}">
      </div>
      <div class="col-12 col-md-6">
        <span class="badge text-bg-secondary mb-2">${producto.categoria}</span>
        <h1 class="h3">${producto.nombre}</h1>
        <p class="fs-3 fw-bold text-danger">${formatearPrecio(producto.precio)}</p>
        <p>${producto.descripcion}</p>
        <button id="btn-agregar" class="btn btn-primary btn-lg">Agregar al carrito</button>
        <a href="index.html" class="btn btn-link">&larr; Seguir comprando</a>
      </div>
    </div>`;

  // Botón "Agregar al carrito" del detalle.
  document.querySelector("#btn-agregar").addEventListener("click", function () {
    agregarAlCarrito(producto.id);
    this.textContent = "¡Agregado!";
    setTimeout(() => {
      this.textContent = "Agregar al carrito";
    }, 1000);
  });
}
