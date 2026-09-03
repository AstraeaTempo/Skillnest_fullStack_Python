import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

# Es indispensable configurar una clave secreta para usar sesiones [cite: 70]
app.secret_key = "clave_secreta_del_destino"


# Ruta Principal GET: Muestra el formulario inicial [cite: 73, 88]
@app.route("/")
def index():
    return render_template("index.html")


# Ruta POST: Procesa el formulario y almacena datos en la sesión [cite: 76, 88, 91]
@app.route("/enviar", methods=["POST"])
def enviar():
    # Se obtienen los valores de los inputs del formulario [cite: 51, 101]
    session["nombre"] = request.form["nombre"]
    session["edad"] = request.form["edad"]
    session["color"] = request.form["color"]
    session["animal"] = request.form["animal"]

    # Redirección con GET para evitar reenviar formularios al recargar [cite: 88, 92]
    return redirect("/futuro")


# Ruta GET: Selecciona un destino aleatorio y renderiza la plantilla [cite: 80, 88, 103]
@app.route("/futuro")
def futuro():
    # Validación básica: si no se ha completado el formulario, redirige al inicio
    if "nombre" not in session:
        return redirect("/")

    # Lista de mensajes de predicción positivos y de prueba [cite: 88]
    predicciones = [
        "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
        "Un gran éxito profesional o académico se aproxima a tu vida pronto.",
        "Ten cuidado con las decisiones apresuradas esta semana, mantén la calma y reflexiona.",
    ]

    # Generación de datos aleatorios para el destino y el número de la suerte [cite: 88, 127]
    prediccion_elegida = random.choice(predicciones)
    numero_suerte = random.randint(1, 100)

    return render_template(
        "futuro.html",
        prediccion=prediccion_elegida,
        numero_suerte=numero_suerte,
    )


if __name__ == "__main__":
    app.run(debug=True)  # [cite: 82, 83, 84]