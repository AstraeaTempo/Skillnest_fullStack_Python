import re
from datetime import datetime, date
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Expresión regular que exige al menos 1 número y 1 mayúscula
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')

class Usuario:
    DB = "bd_registro"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.fecha_nacimiento = data['fecha_nacimiento']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO usuarios (nombre, apellido, email, password, fecha_nacimiento)
        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(fecha_nacimiento)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validar_registro(formulario):
        is_valid = True

        # Validar Nombre
        if len(formulario['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "register")
            is_valid = False
        elif not formulario['nombre'].isalpha():
            flash("El nombre solo debe contener letras.", "register")
            is_valid = False

        # Validar Apellido
        if len(formulario['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "register")
            is_valid = False
        elif not formulario['apellido'].isalpha():
            flash("El apellido solo debe contener letras.", "register")
            is_valid = False

        # Validar Email
        if not EMAIL_REGEX.match(formulario['email']):
            flash("Formato de correo electrónico inválido.", "register")
            is_valid = False
        elif Usuario.get_by_email(formulario['email']):
            flash("El correo electrónico ya está registrado.", "register")
            is_valid = False

        # Validar Fecha de Nacimiento (Mayoría de edad)
        if not formulario['fecha_nacimiento']:
            flash("Debes ingresar tu fecha de nacimiento.", "register")
            is_valid = False
        else:
            fecha_nac = datetime.strptime(formulario['fecha_nacimiento'], "%Y-%m-%d").date()
            hoy = date.today()
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            if edad < 18:
                flash("Debes ser mayor de 18 años para registrarte.", "register")
                is_valid = False

        # Validar Contraseña (Mínimo 8 caracteres, 1 mayúscula, 1 número)
        if len(formulario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "register")
            is_valid = False
        elif not PASSWORD_REGEX.match(formulario['password']):
            flash("La contraseña debe incluir al menos un número y una letra mayúscula.", "register")
            is_valid = False

        # Confirmar Contraseña
        if formulario['password'] != formulario['confirm_password']:
            flash("Las contraseñas no coinciden.", "register")
            is_valid = False

        return is_valid