# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
# Actualización de datos
puntajes[1][0] = 600
print(puntajes)


# Lista de creadores de contenido en una plataforma de streaming--------------------------------------------
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
# Actualización de datos
streamers[0]["nombre"] = "EliteGamerX"
print(streamers[0]["nombre"])


# Eventos en distintas ciudades del mundo-------------------------------------------------------------------
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}
# Actualización de datos
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos["Estados Unidos"][2])


# Coordenadas de la sede de un torneo internacional---------------------------------------------------------
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]
# Actualización de datos
ubicacion[0]["latitud"] = 40.712776
print(ubicacion[0]["latitud"])


#Funciones para recorrer y representar datos:----------------------------------------------------------------
def mostrar_streamers(lista):
    for item in lista:
        print(f"Nombre: {item['nombre']} - Seguidores: {item['seguidores']}")
mostrar_streamers(streamers)

stream = {
    "nombre": ["EliteGamerX", "PixelWarrior"],
    "seguidores": ["250000", "180000"]
}
for separacion, orden in stream.items():
    print(separacion)
    for item in orden:
        print(item)


#Mostrar información de un diccionario con listas:-------------------------------------------------------------
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}
#Diccionario_______________________________________
def mostrar_categorias(diccionario):
    for categoria, items in diccionario.items():
        print(f"{len(items)} {categoria.upper()}")
        for item in items:
            print(item)
mostrar_categorias(categorias)