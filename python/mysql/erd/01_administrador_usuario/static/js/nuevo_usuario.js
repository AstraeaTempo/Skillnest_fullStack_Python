document.addEventListener('DOMContentLoaded', function () {
    
    // Capturamos el formulario por su ID único
    const formNuevoUsuario = document.getElementById('form-nuevo-usuario');

    if (formNuevoUsuario) {
        formNuevoUsuario.addEventListener('submit', function (e) {
            // Evitamos el comportamiento nativo que recarga la página
            e.preventDefault();

            // Obtenemos los valores de las contraseñas introducidas
            const password = document.getElementById('password').value;
            const confPassword = document.getElementById('conf-password').value;

            // Validación de seguridad elemental
            if (password !== confPassword) {
                alert('Las contraseñas no coinciden. Por favor, revísalas e inténtalo de nuevo.');
                return; // Detiene el flujo de la redirección si falla
            }

            // Alerta visual de confirmación para el desarrollador/usuario
            alert('¡Usuario creado correctamente!');
            
            // Redirección al archivo solicitado dentro de la carpeta templates
            window.location.href = 'dashboard_mensajes.html';
        });
    }
});