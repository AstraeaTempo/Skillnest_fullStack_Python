from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/nosotros")
def nosotros():
    return "¡conocenos mejor!"

if __name__ == "__main__":
    app.run(debug=True)