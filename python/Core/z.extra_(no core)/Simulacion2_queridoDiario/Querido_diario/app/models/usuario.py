import re
from app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "querido_diario_db"

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.edad = data['edad']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, edad, password)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(edad)s, %(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results or len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results or len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validar_registro(usuario):
        is_valid = True
        
        # Nombre y Apellido >= 2 caracteres
        if len(usuario.get('nombre', '')) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            is_valid = False
        if len(usuario.get('apellido', '')) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            is_valid = False

        # Email formato válido
        if not EMAIL_REGEX.match(usuario.get('email', '')):
            flash("El correo electrónico debe tener un formato válido.", "registro")
            is_valid = False
        else:
            # Email no duplicado en BD
            user_in_db = Usuario.get_by_email({"email": usuario['email']})
            if user_in_db:
                flash("El correo electrónico ya está registrado.", "registro")
                is_valid = False

        # Edad >= 18 años (BONUS)
        try:
            edad = int(usuario.get('edad', 0))
            if edad < 18:
                flash("Debes tener al menos 18 años para registrarte.", "registro")
                is_valid = False
        except ValueError:
            flash("Por favor ingresa una edad válida.", "registro")
            is_valid = False

        # Contraseña y confirmación coinciden y longitud adecuada
        if len(usuario.get('password', '')) < 6:
            flash("La contraseña debe tener al menos 6 caracteres.", "registro")
            is_valid = False
        if usuario.get('password') != usuario.get('confirm_password'):
            flash("La contraseña y la confirmación deben ser iguales.", "registro")
            is_valid = False

        return is_valid