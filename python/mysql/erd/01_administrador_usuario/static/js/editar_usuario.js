document.getElementById('form-nuevo-usuario').addEventListener('submit', function(event) {
    // Evita la recarga automática del envío predeterminado
    event.preventDefault();

    // Captura de datos modificados
    const nombre = document.getElementById('nombre').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confPassword = document.getElementById('conf-password').value;
    const tipoUsuario = document.getElementById('tipo-usuario').value;

    // Validación de seguridad de contraseñas
    if (password !== confPassword) {
        alert('Error: Las contraseñas ingresadas no coinciden.');
        return;
    }

    // Ventana emergente simulando la persistencia de datos cambiados
    alert(`¡Usuario actualizado correctamente!\n\nNuevos datos registrados:\n• Nombre: ${nombre}\n• E-mail: ${email}\n• Rol del sistema: ${tipoUsuario}`);
});