// Listado de usuarios de prueba cargados en el sistema
const listaUsuarios = [
    { nombre: "Patricia", email: "patricia@codingdojo.com", tipo: "Admin" },
    { nombre: "Andrea", email: "andrea@codingdojo.com", tipo: "Usuario" },
    { nombre: "Katya", email: "katya@codingdojo.com", tipo: "Usuario" }
];

// Renderiza la tabla restringiendo las acciones a solo envío de correos
function renderizarTabla() {
    const tbody = document.getElementById("user-table-body");
    tbody.innerHTML = ""; 

    listaUsuarios.forEach((usuario) => {
        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${usuario.nombre}</td>
            <td>${usuario.email}</td>
            <td>${usuario.tipo}</td>
            <td>
                <button class="btn-action btn-message" style="cursor:pointer; margin-right:5px; background:none; border:none;">💬 Mensaje</button>
            </td>
        `;

        fila.querySelector('.btn-message').addEventListener('click', () => {
                // Redirige al formulario de envío de mensajes
                window.location.href = 'enviar_mensaje.html';
            });

        tbody.appendChild(fila);
    });
}

// Acción del botón de mensaje
function abrirMensajero(email) {
    alert(`Abriendo cliente de mensajería para: ${email}`);
}

// Cargar los datos al inicializar la ventana
window.onload = renderizarTabla;