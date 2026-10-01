import re
from app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "bookhub_db"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'email': email})
        if not results or len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'id': user_id})
        if not results:
            return False
        return cls(results[0])

    @staticmethod
    def validate_register(data):
        is_valid = True

        if len(data['first_name'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "register_error")
            is_valid = False

        if len(data['last_name'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "register_error")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("Formato de correo electrónico inválido.", "register_error")
            is_valid = False
        else:
            if User.get_by_email(data['email']):
                flash("El correo electrónico ya está registrado.", "register_error")
                is_valid = False

        if len(data['password']) < 6:
            flash("La contraseña debe tener al menos 6 caracteres.", "register_error")
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash("Las contraseñas no coinciden.", "register_error")
            is_valid = False

        return is_valid