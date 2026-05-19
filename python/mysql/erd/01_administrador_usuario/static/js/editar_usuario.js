document.addEventListener('DOMContentLoaded', function () {
    
    // Buscamos el formulario de edición por su ID
    const formEditar = document.getElementById('form-editar-usuario');

    if (formEditar) {
        formEditar.addEventListener('submit', function (e) {
            // Evitamos que la página se recargue inmediatamente
            e.preventDefault();

            // Capturamos las contraseñas para verificar que coincidan
            const password = document.getElementById('password').value;
            const confPassword = document.getElementById('conf-password').value;

            // Validación: Verificar que las contraseñas coincidan antes de avanzar
            if (password !== confPassword) {
                alert('Las contraseñas no coinciden. Por favor, verifícalas antes de guardar.');
                return; // Detiene el código si hay error
            }

            // Si pasa la validación, confirmamos el éxito y redirigimos
            alert('¡Usuario actualizado con éxito!');
            
            // Redirección al archivo deseado (asumiendo que están en la misma carpeta templates)
            window.location.href = 'dashboard_mensajes.html';
        });
    }
});