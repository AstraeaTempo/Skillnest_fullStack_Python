from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)

# ==========================================================
# RUTAS DE LA APLICACIÓN
# ==========================================================

@app.route("/usuarios")
def usuarios():
    """
    Muestra la lista completa de usuarios.
    """
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)


@app.route("/usuarios/nuevo")
def nuevo_usuario():
    """
    Muestra el formulario para registrar un nuevo usuario.
    """
    return render_template("usuario_nuevo.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    """
    Procesa el formulario de registro y guarda los datos mediante POST.
    """
    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    email = request.form["email"].strip()

    # Validación básica
    if not nombre or not apellido or not email:
        return render_template(
            "usuario_nuevo.html",
            error="Todos los campos son obligatorios."
        )

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }

    resultado = Usuario.save(data)

    if resultado is False:
        return render_template(
            "usuario_nuevo.html",
            error="No fue posible guardar el usuario en la base de datos."
        )

    # Patrón POST -> Redirect -> GET
    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)