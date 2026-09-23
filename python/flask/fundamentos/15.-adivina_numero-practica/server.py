# ==========================================================
# ADIVINA EL NÚMERO
# Juego desarrollado con Flask
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)
import random

app = Flask(__name__)

# Clave secreta necesaria para manejar variables en session
app.secret_key = "clave-secreta-adivina-numero"

# ----------------------------------------------------------
# RUTA PRINCIPAL
# ----------------------------------------------------------
@app.route("/")
def index():
    """
    Muestra la página principal del juego e inicializa
    las variables dentro de la sesión si no existen.
    """
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 10)

    if "intentos" not in session:
        session["intentos"] = 0

    if "mensaje" not in session:
        session["mensaje"] = "Adivina un número entre 1 y 10."

    if "resultado" not in session:
        session["resultado"] = ""

    return render_template(
        "index.html",
        mensaje=session["mensaje"],
        resultado=session["resultado"],
        intentos=session["intentos"]
    )

# ----------------------------------------------------------
# PROCESAR INTENTO
# ----------------------------------------------------------
@app.route("/adivinar", methods=["POST"])
def adivinar():
    """
    Procesa el número ingresado por el usuario y
    actualiza las variables de estado en la sesión.
    """
    numero = int(request.form["numero"])
    numero_secreto = session["numero_secreto"]

    session["intentos"] += 1

    if numero < numero_secreto:
        session["mensaje"] = f"El número secreto es mayor que {numero}."
        session["resultado"] = "mayor"
    elif numero > numero_secreto:
        session["mensaje"] = f"El número secreto es menor que {numero}."
        session["resultado"] = "menor"
    else:
        session["mensaje"] = f"¡Correcto! El número secreto era {numero_secreto}."
        session["resultado"] = "correcto"

    return redirect(url_for("index"))

# ----------------------------------------------------------
# REINICIAR JUEGO
# ----------------------------------------------------------
@app.route("/reiniciar")
def reiniciar():
    """
    Elimina la información almacenada en sesión
    para comenzar una nueva partida.
    """
    session.clear()
    return redirect(url_for("index"))

# ----------------------------------------------------------
# EJECUCIÓN
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)