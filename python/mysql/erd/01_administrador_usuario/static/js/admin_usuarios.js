// Arreglo de datos que simula la base de datos de usuarios
const usuarios = [
    { nombre: "Patricia", email: "patricia@codingdojo.com", tipo: "Admin" },
    { nombre: "Andrea", email: "andrea@codingdojo.com", tipo: "Usuario" },
    { nombre: "Katya", email: "katya@codingdojo.com", tipo: "Usuario" }
];

// Función para renderizar la lista de usuarios en la tabla HTML
function cargarUsuarios() {
    const tableBody = document.getElementById("user-table-body");
    tableBody.innerHTML = ""; // Limpiar contenido previo

    usuarios.forEach((usuario, index) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${usuario.nombre}</td>
            <td>${usuario.email}</td>
            <td>${usuario.tipo}</td>
            <td>
                <div class="actions-cell">
                    <span class="action-icon" title="Editar" onclick="editarUsuario(${index})">✏️</span>
                    <span class="action-icon" title="Borrar" onclick="borrarUsuario(${index})">🗑️</span>
                    <span class="action-icon" title="Mensaje" onclick="enviarMensaje(${index})">✉️</span>
                </div>
            </td>
        `;

        tableBody.appendChild(row);
    });
}

// Evento para el botón "Nuevo Usuario"
document.getElementById("btn-nuevo").addEventListener("click", () => {
    alert("Acción: Crear un nuevo usuario");
});

// Funciones interactivas para simular los botones de acciones
function editarUsuario(index) {
    alert(`Editar al usuario: ${usuarios[index].nombre}`);
}

function borrarUsuario(index) {
    const confirmar = confirm(`¿Estás seguro de que deseas borrar a ${usuarios[index].nombre}?`);
    if (confirmar) {
        usuarios.splice(index, 1); // Remover del arreglo
        cargarUsuarios(); // Volver a pintar la tabla
    }
}

function enviarMensaje(index) {
    alert(`Enviar correo electrónico a: ${usuarios[index].email}`);
}

// Inicializar la carga al abrir la página
window.onload = cargarUsuarios;