from app import app
from app.controllers import usuarios_controller, peliculas_controller

if __name__ == "__main__":
    app.run(debug=True)