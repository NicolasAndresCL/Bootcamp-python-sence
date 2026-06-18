// ============================================================
// home.js  -  Renderiza la grilla de productos del inicio
// ============================================================

const grillaProductos = document.querySelector("#grilla-productos");

// Crea el HTML de una card (tarjeta) a partir de un producto.
function crearCard(producto) {
  return `
    <div class="col-12 col-sm-6 col-lg-4 col-xl-3">
      <article class="card h-100 shadow-sm">
        <img src="${producto.imagen}" class="card-img-top" alt="${producto.nombre}">
        <div class="card-body d-flex flex-column">
          <span class="badge text-bg-secondary align-self-start mb-2">${producto.categoria}</span>
          <h3 class="card-title h5">${producto.nombre}</h3>
          <p class="card-text fw-bold text-danger fs-5">${formatearPrecio(producto.precio)}</p>
          <div class="mt-auto d-grid gap-2">
            <a href="detalle.html?id=${producto.id}" class="btn btn-outline-dark">Ver más</a>
            <button class="btn btn-primary" data-id="${producto.id}">Agregar al carrito</button>
          </div>
        </div>
      </article>
    </div>`;
}

// Recorre todos los productos y los pinta en la grilla.
function renderizarProductos() {
  grillaProductos.innerHTML = PRODUCTOS.map(crearCard).join("");
}

// Un solo listener para todos los botones "Agregar" (delegación de eventos).
grillaProductos.addEventListener("click", function (evento) {
  const boton = evento.target.closest("button[data-id]");
  if (!boton) {
    return; // el clic no fue en un botón "Agregar"
  }

  const id = Number(boton.dataset.id);
  agregarAlCarrito(id);

  // Pequeña confirmación visual.
  boton.textContent = "¡Agregado!";
  setTimeout(function () {
    boton.textContent = "Agregar al carrito";
  }, 1000);
});

renderizarProductos();
