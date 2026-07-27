#Inicio.-----------------------------------------------------------------------------------------------------
from flask import Flask, render_template

app = Flask(__name__)

#Pokemons----------------------------------------------------------------------------------------------------
pokedex = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]


#1-Ruta que muestra todos los pokemons-----------------------------------------------------------------------
@app.route("/")
@app.route("/pokemon")
def index():
    return render_template(
        "pokemon.html", 
        pokemons=pokedex, 
        titulo="Pokédex"
    )

#2-Muestra una cantidad especifica---------------------------------------------------------------------------
@app.route("/pokemon/cantidad/<int:cantidad>")
def limite_pokemon(cantidad):
    return render_template(
        "pokemon.html", 
        pokemons=pokedex[:cantidad], 
        titulo=f"Primeros {cantidad} Pokémon"
    )

#3-Muestra pokemon con ID------------------------------------------------------------------------------------
@app.route("/pokemon/<int:id>")
def pokemon_por_id(id):
    pokemon = next((p for p in pokedex if p["id"] == id), None)
    if not pokemon:
        return pokemon_no_encontrado(f"No se encontró ningún Pokémon con el ID #{id}.")
    return render_template(
        "pokemon.html",
        pokemon=pokemon,
        titulo=pokemon["nombre"]
    )

#4-Pokemon por nombre----------------------------------------------------------------------------------------
@app.route("/pokemon/<string:nombre>")
def pokemon_por_nombre(nombre):
    pokemon = next((p for p in pokedex if p["nombre"].lower() == nombre.lower()), None)
    if not pokemon:
        return pokemon_no_encontrado(f"No se encontró ningún Pokémon llamado '{nombre}'.")
    return render_template(
        "pokemon.html", 
        pokemon=pokemon, 
        titulo=pokemon["nombre"]
    )

#5-Error404 pokemon no encontrado----------------------------------------------------------------------------
def pokemon_no_encontrado(mensaje: str):
    return render_template("404.html", mensaje=mensaje), 404

if __name__ == "__main__":
    app.run(debug=True)

#sorry but this doesn´t work (for me)