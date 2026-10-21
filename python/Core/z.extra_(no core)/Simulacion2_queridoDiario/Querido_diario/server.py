from app import app
from app.controllers import usuarios, entradas

if __name__ == "__main__":
    app.run(debug=True, port=5000)