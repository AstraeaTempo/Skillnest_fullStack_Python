from app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Book:
    DB = "bookhub_db"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.genre = data['genre']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_name = data.get('user_name', '')
        self.favorites_count = data.get('favorites_count', 0)

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO books (title, author, genre, release_date, description, user_id)
        VALUES (%(title)s, %(author)s, %(genre)s, %(release_date)s, %(description)s, %(user_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE books 
        SET title = %(title)s, author = %(author)s, genre = %(genre)s, 
            release_date = %(release_date)s, description = %(description)s 
        WHERE id = %(id)s AND user_id = %(user_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, book_id, user_id):
        query = "DELETE FROM books WHERE id = %(id)s AND user_id = %(user_id)s;"
        return connectToMySQL(cls.DB).query_db(query, {'id': book_id, 'user_id': user_id})

    @classmethod
    def get_by_user(cls, user_id):
        query = """
        SELECT b.*, COUNT(f.user_id) as favorites_count 
        FROM books b
        LEFT JOIN favorites f ON b.id = f.book_id
        WHERE b.user_id = %(user_id)s
        GROUP BY b.id;
        """
        results = connectToMySQL(cls.DB).query_db(query, {'user_id': user_id})
        books = []
        if results:
            for row in results:
                books.append(cls(row))
        return books

    @classmethod
    def get_community_books(cls, user_id):
        query = """
        SELECT b.*, CONCAT(u.first_name, ' ', u.last_name) as user_name, COUNT(f.user_id) as favorites_count
        FROM books b
        JOIN users u ON b.user_id = u.id
        LEFT JOIN favorites f ON b.id = f.book_id
        WHERE b.user_id != %(user_id)s
        GROUP BY b.id;
        """
        results = connectToMySQL(cls.DB).query_db(query, {'user_id': user_id})
        books = []
        if results:
            for row in results:
                books.append(cls(row))
        return books

    @classmethod
    def get_by_id(cls, book_id):
        query = """
        SELECT b.*, CONCAT(u.first_name, ' ', u.last_name) as user_name, COUNT(f.user_id) as favorites_count
        FROM books b
        JOIN users u ON b.user_id = u.id
        LEFT JOIN favorites f ON b.id = f.book_id
        WHERE b.id = %(id)s
        GROUP BY b.id;
        """
        results = connectToMySQL(cls.DB).query_db(query, {'id': book_id})
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def add_favorite(cls, user_id, book_id):
        query = "INSERT IGNORE INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(cls.DB).query_db(query, {'user_id': user_id, 'book_id': book_id})

    @classmethod
    def is_favorited_by_user(cls, user_id, book_id):
        query = "SELECT * FROM favorites WHERE user_id = %(user_id)s AND book_id = %(book_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'user_id': user_id, 'book_id': book_id})
        return len(results) > 0 if results else False

    @classmethod
    def get_favorited_users(cls, book_id):
        query = """
        SELECT u.id, CONCAT(u.first_name, ' ', u.last_name) as name
        FROM users u
        JOIN favorites f ON u.id = f.user_id
        WHERE f.book_id = %(book_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, {'book_id': book_id})

    @classmethod
    def get_user_favorites(cls, user_id):
        query = """
        SELECT b.*, CONCAT(u.first_name, ' ', u.last_name) as user_name
        FROM books b
        JOIN favorites f ON b.id = f.book_id
        JOIN users u ON b.user_id = u.id
        WHERE f.user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, {'user_id': user_id})
        books = []
        if results:
            for row in results:
                books.append(cls(row))
        return books

    @staticmethod
    def validate_book(data):
        is_valid = True

        if len(data['title'].strip()) < 2:
            flash("El título debe tener al menos 2 caracteres.", "book_error")
            is_valid = False

        if len(data['author'].strip()) < 2:
            flash("El autor debe tener al menos 2 caracteres.", "book_error")
            is_valid = False

        if not data.get('genre'):
            flash("Debes seleccionar un género.", "book_error")
            is_valid = False

        if not data.get('release_date'):
            flash("Debes ingresar una fecha de publicación.", "book_error")
            is_valid = False
        else:
            try:
                pub_date = datetime.strptime(data['release_date'], '%Y-%m-%d').date()
                if pub_date > datetime.now().date():
                    flash("La fecha de publicación no puede ser pasada en el futuro.", "book_error")
                    is_valid = False
            except ValueError:
                flash("Formato de fecha inválido.", "book_error")
                is_valid = False

        if len(data['description'].strip()) < 10:
            flash("La descripción debe tener al menos 10 caracteres.", "book_error")
            is_valid = False

        return is_valid