from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/nosotros")
def nosotros():
    return "¡conocenos mejor!"

@app.route("/shalki")
def shalki():
    return "viva la vida!"

@app.route("/jestty")
def jestty():
    return "¡Los demás te escondieron muy bien… ¡No podía encontrarte y ya me estaba desesperando JA!"

if __name__ == "__main__":
    app.run(debug=True)