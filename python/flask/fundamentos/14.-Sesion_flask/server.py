# ==========================================
# IMPORTACIONES
# ==========================================

from flask import Flask, render_template, request, redirect, session


# ==========================================
# CREAR APLICACIÓN
# ==========================================

app = Flask(__name__)


# ==========================================
# CLAVE SECRETA
# ==========================================

app.secret_key = "una-clave-secreta"


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario de creación de usuario.
    """
    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO
# ==========================================

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    """
    Recibe los datos enviados mediante POST y los almacena en la sesión.
    """
    nombre = request.form["nombre"]
    email = request.form["email"]

    print("===================================")
    print("Información recibida")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print("===================================")

    session["nombre_usuario"] = nombre
    session["email_usuario"] = email

    return redirect("/mostrar_usuario")


# ==========================================
# MOSTRAR USUARIO
# ==========================================

@app.route("/mostrar_usuario")
def mostrar_usuario():
    """
    Recupera la información almacenada en la sesión y renderiza la plantilla.
    """
    nombre = session.get("nombre_usuario")
    email = session.get("email_usuario")

    print("===================================")
    print("Usuario redirigido")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print("===================================")

    return render_template("mostrar.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)