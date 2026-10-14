from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    DB = "cinepedia_schema"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if not result or len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if not result or len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validar_registro(usuario):
        is_valid = True
        if len(usuario.get('nombre', '')) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "register")
            is_valid = False
        if len(usuario.get('apellido', '')) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(usuario.get('email', '')):
            flash("El email debe tener un formato válido.", "register")
            is_valid = False
        else:
            if Usuario.get_by_email({"email": usuario['email']}):
                flash("El email ya se encuentra registrado.", "register")
                is_valid = False
        if len(usuario.get('password', '')) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "register")
            is_valid = False
        if usuario.get('password') != usuario.get('confirm_password'):
            flash("Las contraseñas no coinciden.", "register")
            is_valid = False
        return is_valid