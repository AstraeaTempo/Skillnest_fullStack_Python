from datetime import datetime
from app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = "querido_diario_db"

class Entrada:
    def __init__(self, data):
        self.id = data['id']
        self.fecha_entrada = data['fecha_entrada']
        self.notas = data['notas']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO entradas (fecha_entrada, notas, usuario_id)
            VALUES (%(fecha_entrada)s, %(notas)s, %(usuario_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_user(cls, data):
        # Despliega entradas en orden de más reciente a más antigua (BONUS)
        query = "SELECT * FROM entradas WHERE usuario_id = %(usuario_id)s ORDER BY fecha_entrada DESC;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        entradas = []
        if results:
            for row in results:
                entradas.append(cls(row))
        return entradas

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM entradas WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results or len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
            UPDATE entradas 
            SET fecha_entrada = %(fecha_entrada)s, notas = %(notas)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM entradas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def search_by_notes(cls, data):
        # Búsqueda por término en notas[cite: 2]
        query = """
            SELECT * FROM entradas 
            WHERE usuario_id = %(usuario_id)s AND notas LIKE %(termino)s 
            ORDER BY fecha_entrada DESC;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        entradas = []
        if results:
            for row in results:
                entradas.append(cls(row))
        return entradas

    @staticmethod
    def validar_entrada(data):
        is_valid = True
        
        # Fecha y notas obligatorias / notas no vacías[cite: 2]
        if not data.get('fecha_entrada'):
            flash("La fecha no puede estar vacía.", "entrada")
            is_valid = False
        else:
            # Validar que no sea una fecha en el futuro (BONUS)[cite: 2]
            try:
                fecha_ingresada = datetime.strptime(data['fecha_entrada'], '%Y-%m-%d').date()
                if fecha_ingresada > datetime.now().date():
                    flash("No puedes ingresar una fecha en el futuro.", "entrada")
                    is_valid = False
            except ValueError:
                flash("Formato de fecha inválido.", "entrada")
                is_valid = False

        if not data.get('notas') or len(data['notas'].strip()) == 0:
            flash("Las notas no pueden estar vacías.", "entrada")
            is_valid = False

        return is_valid