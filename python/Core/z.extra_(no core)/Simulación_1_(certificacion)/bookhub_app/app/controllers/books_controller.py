from app import app
from flask import render_template, redirect, request, session, flash
from app.models.book_model import Book
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/libros")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    
    my_books = Book.get_by_user(session["user_id"])
    community_books = Book.get_community_books(session["user_id"])
    return render_template("dashboard.html", my_books=my_books, community_books=community_books)

@app.route("/libros/nuevo")
def new_book():
    if "user_id" not in session:
        return redirect("/")
    return render_template("new_book.html")

@app.route("/libros/crear", methods=["POST"])
def create_book():
    if "user_id" not in session:
        return redirect("/")
    
    if not Book.validate_book(request.form):
        return redirect("/libros/nuevo")

    data = {
        "title": request.form["title"].strip(),
        "author": request.form["author"].strip(),
        "genre": request.form["genre"],
        "release_date": request.form["release_date"],
        "description": request.form["description"].strip(),
        "user_id": session["user_id"]
    }
    Book.save(data)
    return redirect("/libros")

@app.route("/libros/<int:book_id>")
def show_book(book_id):
    if "user_id" not in session:
        return redirect("/")

    book = Book.get_by_id(book_id)
    if not book:
        return redirect("/libros")

    is_favorited = Book.is_favorited_by_user(session["user_id"], book_id)
    favorited_users = Book.get_favorited_users(book_id)
    return render_template("show_book.html", book=book, is_favorited=is_favorited, favorited_users=favorited_users)

@app.route("/libros/editar/<int:book_id>")
def edit_book(book_id):
    if "user_id" not in session:
        return redirect("/")

    book = Book.get_by_id(book_id)
    if not book or book.user_id != session["user_id"]:
        return redirect("/libros")

    return render_template("edit_book.html", book=book)

@app.route("/libros/actualizar/<int:book_id>", methods=["POST"])
def update_book(book_id):
    if "user_id" not in session:
        return redirect("/")

    book = Book.get_by_id(book_id)
    if not book or book.user_id != session["user_id"]:
        return redirect("/libros")

    if not Book.validate_book(request.form):
        return redirect(f"/libros/editar/{book_id}")

    data = {
        "id": book_id,
        "title": request.form["title"].strip(),
        "author": request.form["author"].strip(),
        "genre": request.form["genre"],
        "release_date": request.form["release_date"],
        "description": request.form["description"].strip(),
        "user_id": session["user_id"]
    }
    Book.update(data)
    return redirect("/libros")

@app.route("/libros/eliminar/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    if "user_id" not in session:
        return redirect("/")

    Book.delete(book_id, session["user_id"])
    return redirect("/libros")

@app.route("/favoritos/agregar/<int:book_id>", methods=["POST"])
def add_favorite(book_id):
    if "user_id" not in session:
        return redirect("/")

    Book.add_favorite(session["user_id"], book_id)
    return redirect(f"/libros/{book_id}")

@app.route("/favoritos")
def favorites():
    if "user_id" not in session:
        return redirect("/")

    favorite_books = Book.get_user_favorites(session["user_id"])
    return render_template("favorites.html", books=favorite_books)