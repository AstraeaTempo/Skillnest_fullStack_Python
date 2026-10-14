from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pelicula:
    DB = "cinepedia_schema"

    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.director = data['director']
        self.fecha_estreno = data['fecha_estreno']
        self.sinopsis = data['sinopsis']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creador = data.get('creador', None)

    @classmethod
    def save(cls, data):
        query = """INSERT INTO peliculas (titulo, director, fecha_estreno, sinopsis, usuario_id) 
                   VALUES (%(titulo)s, %(director)s, %(fecha_estreno)s, %(sinopsis)s, %(usuario_id)s);"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """SELECT peliculas.*, usuarios.nombre AS creador_nombre 
                   FROM peliculas JOIN usuarios ON peliculas.usuario_id = usuarios.id;"""
        results = connectToMySQL(cls.DB).query_db(query)
        peliculas = []
        if results:
            for row in results:
                pelicula = cls(row)
                pelicula.creador = row['creador_nombre']
                peliculas.append(pelicula)
        return peliculas

    @classmethod
    def get_by_id(cls, data):
        query = """SELECT peliculas.*, usuarios.nombre AS creador_nombre 
                   FROM peliculas JOIN usuarios ON peliculas.usuario_id = usuarios.id 
                   WHERE peliculas.id = %(id)s;"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        if not result:
            return False
        pelicula = cls(result[0])
        pelicula.creador = result[0]['creador_nombre']
        return pelicula

    @classmethod
    def get_by_titulo(cls, data):
        query = "SELECT * FROM peliculas WHERE titulo = %(titulo)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result and len(result) > 0:
            return cls(result[0])
        return False

    @classmethod
    def update(cls, data):
        query = """UPDATE peliculas SET titulo=%(titulo)s, director=%(director)s, 
                   fecha_estreno=%(fecha_estreno)s, sinopsis=%(sinopsis)s 
                   WHERE id=%(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM peliculas WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validar_pelicula(pelicula, pelicula_id=None):
        is_valid = True
        if len(pelicula.get('titulo', '').strip()) < 3:
            flash("El Nombre de Peli debe tener al menos 3 caracteres.", "pelicula")
            is_valid = False
        else:
            existente = Pelicula.get_by_titulo({"titulo": pelicula['titulo'].strip()})
            if existente and str(existente.id) != str(pelicula_id):
                flash("El nombre de la película debe ser único.", "pelicula")
                is_valid = False

        if len(pelicula.get('director', '').strip()) < 3:
            flash("El Director debe tener al menos 3 caracteres.", "pelicula")
            is_valid = False

        if not pelicula.get('fecha_estreno'):
            flash("Fecha Estreno no puede estar vacía.", "pelicula")
            is_valid = False

        if len(pelicula.get('sinopsis', '').strip()) < 3:
            flash("Sinopsis no puede estar vacía y debe tener al menos 3 caracteres.", "pelicula")
            is_valid = False

        return is_valid