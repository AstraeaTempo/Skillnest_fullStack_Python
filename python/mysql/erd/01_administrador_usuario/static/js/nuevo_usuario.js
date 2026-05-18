document.getElementById('form-nuevo-usuario').addEventListener('submit', function(event) {
    // Evita que la página se recargue automáticamente al enviar
    event.preventDefault();

    // Captura de los valores de los inputs
    const nombre = document.getElementById('nombre').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confPassword = document.getElementById('conf-password').value;
    const tipoUsuario = document.getElementById('tipo-usuario').value;

    // Validación básica: que las contraseñas coincidan
    if (password !== confPassword) {
        alert('Error: Las contraseñas no coinciden.');
        return;
    }

    // Simulación de éxito de creación de datos
    alert(`¡Usuario creado con éxito!\n\nNombre: ${nombre}\nE-mail: ${email}\nTipo: ${tipoUsuario}`);
    
    // Opcional: Limpiar el formulario tras la creación exitosa
    this.reset();
});