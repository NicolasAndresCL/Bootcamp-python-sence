// ============================================================
// productos.js  -  Datos y lógica compartida del e-commerce
// ============================================================
// Este archivo se incluye en TODAS las páginas. Contiene:
//  - El catálogo de productos (un arreglo de objetos).
//  - Funciones para manejar el carrito usando localStorage,
//    de modo que el carrito se mantenga al cambiar de página.
//  - La función que actualiza el contador (badge) del navbar.

// Catálogo: cada producto es un objeto con sus propiedades.
const PRODUCTOS = [
  {
    id: 1,
    nombre: "Telescopio Orion 90",
    categoria: "telescopios",
    precio: 129990,
    descripcion: "Telescopio refractor de 90 mm ideal para iniciarse en la astronomía. Incluye trípode y dos oculares.",
    imagen: "https://placehold.co/600x400/0b1d3a/ffffff?text=Telescopio",
  },
  {
    id: 2,
    nombre: "Maqueta Apolo 11",
    categoria: "maquetas",
    precio: 34990,
    descripcion: "Réplica a escala del cohete Saturno V de la misión Apolo 11. Para armar y exhibir.",
    imagen: "https://placehold.co/600x400/1b3a5c/ffffff?text=Apolo+11",
  },
  {
    id: 3,
    nombre: "Casco de Astronauta",
    categoria: "coleccionables",
    precio: 79990,
    descripcion: "Réplica decorativa del casco de un traje espacial. Pieza de colección de tamaño real.",
    imagen: "https://placehold.co/600x400/2a4d6e/ffffff?text=Casco",
  },
  {
    id: 4,
    nombre: "Globo Lunar LED",
    categoria: "decoración",
    precio: 24990,
    descripcion: "Lámpara con forma de Luna y textura realista. Luz cálida regulable por contacto.",
    imagen: "https://placehold.co/600x400/0b1d3a/ffffff?text=Luna+LED",
  },
  {
    id: 5,
    nombre: "Set de Cohetes a Escala",
    categoria: "maquetas",
    precio: 19990,
    descripcion: "Colección de 3 cohetes históricos para armar. Incluye base y fichas informativas.",
    imagen: "https://placehold.co/600x400/1b3a5c/ffffff?text=Cohetes",
  },
  {
    id: 6,
    nombre: "Planetario de Escritorio",
    categoria: "decoración",
    precio: 44990,
    descripcion: "Proyector que muestra estrellas y nebulosas en el techo. Perfecto para relajarse.",
    imagen: "https://placehold.co/600x400/2a4d6e/ffffff?text=Planetario",
  },
  {
    id: 7,
    nombre: "Mochila Galaxy",
    categoria: "accesorios",
    precio: 29990,
    descripcion: "Mochila resistente con estampado de galaxia y compartimento acolchado para notebook.",
    imagen: "https://placehold.co/600x400/1b3a5c/ffffff?text=Mochila",
  },
  {
    id: 8,
    nombre: "Póster Vía Láctea",
    categoria: "decoración",
    precio: 9990,
    descripcion: "Impresión de alta calidad de la Vía Láctea sobre papel mate. Tamaño 50 x 70 cm.",
    imagen: "https://placehold.co/600x400/0b1d3a/ffffff?text=Poster",
  },
];

// ------------------------------------------------------------
// Utilidades
// ------------------------------------------------------------

// Da formato de precio en pesos chilenos: 129990 -> "$129.990"
function formatearPrecio(valor) {
  return "$" + valor.toLocaleString("es-CL");
}

// Busca un producto por su id dentro del catálogo.
function buscarProducto(id) {
  return PRODUCTOS.find((producto) => producto.id === id);
}

// ------------------------------------------------------------
// Carrito (guardado en localStorage)
// ------------------------------------------------------------
// En el carrito guardamos solo { id, cantidad }; los datos del
// producto se obtienen del catálogo cuando se necesitan.

function obtenerCarrito() {
  const datos = localStorage.getItem("carrito");
  // Si no hay nada guardado, devolvemos un arreglo vacío.
  return datos ? JSON.parse(datos) : [];
}

function guardarCarrito(carrito) {
  localStorage.setItem("carrito", JSON.stringify(carrito));
}

function agregarAlCarrito(idProducto) {
  const carrito = obtenerCarrito();
  const item = carrito.find((elemento) => elemento.id === idProducto);

  if (item) {
    // Si el producto ya estaba, solo sumamos una unidad.
    item.cantidad += 1;
  } else {
    // Si no estaba, lo agregamos con cantidad 1.
    carrito.push({ id: idProducto, cantidad: 1 });
  }

  guardarCarrito(carrito);
  actualizarContador();
}

// Suma la cantidad total de unidades en el carrito.
function contarItems() {
  const carrito = obtenerCarrito();
  let total = 0;
  for (const item of carrito) {
    total += item.cantidad;
  }
  return total;
}

// Actualiza el número que se muestra en el badge del navbar.
function actualizarContador() {
  const badge = document.querySelector("#contador-carrito");
  if (badge) {
    badge.textContent = contarItems();
  }
}

// Al cargar cualquier página, mostramos el contador correcto.
document.addEventListener("DOMContentLoaded", actualizarContador);
