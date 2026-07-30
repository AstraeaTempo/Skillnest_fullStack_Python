from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales------------------------------------
datos = [
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "icon": "discord"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "icon": "instagram"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "icon": "netflix"},
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "icon": "spotify"},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "icon": "tiktok"},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "icon": "twitch"},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "icon": "youtube"},
]

# Ruta para mostrar la tabla con datos-----------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', plataformas=datos)

if __name__ == "__main__":
    app.run(debug=True)