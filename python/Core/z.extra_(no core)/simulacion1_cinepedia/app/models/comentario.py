from app.config.mysqlconnection import connectToMySQL

class Comentario:
    DB = "cinepedia_schema"

    def __init__(self, data):
        self.id = data['id']
        self.contenido = data['contenido']
        self.usuario_id = data['usuario_id']
        self.pelicula_id = data['pelicula_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.autor = data.get('autor', None)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comentarios (contenido, usuario_id, pelicula_id) VALUES (%(contenido)s, %(usuario_id)s, %(pelicula_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_pelicula(cls, data):
        query = """SELECT comentarios.*, usuarios.nombre AS autor_nombre 
                FROM comentarios JOIN usuarios ON comentarios.usuario_id = usuarios.id 
                WHERE pelicula_id = %(pelicula_id)s ORDER BY comentarios.created_at DESC;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        comentarios = []
        if results:
            for row in results:
                comentario = cls(row)
                comentario.autor = row['autor_nombre']
                comentarios.append(comentario)
        return comentarios

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM comentarios WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM comentarios WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result and len(result) > 0:
            return cls(result[0])
        return False