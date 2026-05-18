document.addEventListener("DOMContentLoaded", () => {
    // Vistas principales
    const authView = document.getElementById("auth-view");
    const adminView = document.getElementById("admin-view");

    // Formularios
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");

    // Evento al presionar "Iniciar Sesión"
    loginForm.addEventListener("submit", (e) => {
        e.preventDefault(); // Evita que la página se recargue

        // Aquí podrías validar credenciales si lo necesitas
        authView.classList.add("hidden");  // Oculta login/registro
        adminView.classList.remove("hidden"); // Muestra la tabla del dashboard
    });

    // Evento al presionar "Registrar"
    registerForm.addEventListener("submit", (e) => {
        e.preventDefault(); // Evita que la página se recargue

        // Validación simple de contraseñas idénticas
        const pass = document.getElementById("reg-password").value;
        const confirmPass = document.getElementById("reg-confirm").value;

        if (pass !== confirmPass) {
            alert("Las contraseñas no coinciden.");
            return;
        }

        authView.classList.add("hidden");
        adminView.classList.remove("hidden");
    });
});
