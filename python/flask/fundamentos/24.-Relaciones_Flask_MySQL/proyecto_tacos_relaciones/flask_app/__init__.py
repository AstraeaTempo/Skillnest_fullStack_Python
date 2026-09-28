# ==========================================================
# INICIALIZACIÓN DE FLASK
# ==========================================================

from flask import Flask

app = Flask(__name__)

# Clave secreta para manejo de sesiones o mensajes flash
app.secret_key = "clave-secreta-desarrollo-tacos"