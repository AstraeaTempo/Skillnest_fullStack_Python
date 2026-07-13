#Practica
from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio ------------------------------------ 1
@app.route("/")
def inicio():
    return "<h1>🌎 ¡Bienvenido a nuestro servidor Flask!</h1>"

# Ruta genérica para explorar enrutamiento -------------------------2
@app.route("/explorar")
def explorar():
    return "🔍 ¿Qué ruta estás buscando? ¡Prueba con diferentes direcciones!"

# Rutas dinámicas para personalización -----------------------------3
@app.route("/perfil/<nombre>")
def perfil(nombre):
    return f"👤 Bienvenid@ {nombre} a tu perfil personalizado en nuestra app."

# Ruta que repite un mensaje varias veces --------------------------4
@app.route("/repite/<int:veces>/<mensaje>")
def repite(veces, mensaje):
    return f"Repite después de mí: {mensaje}. " * veces

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente ----5
@app.route("/error")
def error():
    return "⚠️ ¡Sobrecarga de rutas! No encontramos a dónde quieres ir, inténtalo de nuevo."

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)