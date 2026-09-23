# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================

from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)


@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de datos
    y las envía hacia la plantilla HTML.
    """
    mascotas = Mascota.get_all()

    print(mascotas)

    return render_template(
        "index.html",
        mascotas=mascotas
    )


if __name__ == "__main__":
    app.run(debug=True)