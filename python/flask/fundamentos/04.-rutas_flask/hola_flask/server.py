from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>¡Hello world!</h1><p>this is a text</p>"

@app.route("/exito")
def exito():
    return "¡Exito!"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hello {nombre}!"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return f"Hello {nombre}, your favorite color is {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return f"¡Hola {nombre}!" * veces

@app.route("/hi") #conchetes angulares.
def hi():
    return "<h1>hellos everyone! ready to start the show?</h1> <p>and I have a special guest! is a new player!</p>"

#desafio 1
@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"¡Hasta luego {nombre}! ¡Esperamos verte pronto!"

#desafio 2
@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años."

if __name__ == "__main__":
    app.run(debug=True)