from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "clave_secreta_querido_diario"

# Manejo de error 404 opcional
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"), 404