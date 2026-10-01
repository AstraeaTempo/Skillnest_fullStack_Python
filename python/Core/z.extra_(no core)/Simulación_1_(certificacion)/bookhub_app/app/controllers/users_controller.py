from app import app
from flask import render_template, redirect, request, session, flash
from app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/libros")
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
    data = {
        "first_name": request.form["first_name"].strip(),
        "last_name": request.form["last_name"].strip(),
        "email": request.form["email"].strip().lower(),
        "password": pw_hash
    }
    user_id = User.save(data)
    session["user_id"] = user_id
    session["user_name"] = data["first_name"]
    return redirect("/libros")

@app.route("/login", methods=["POST"])
def login():
    user = User.get_by_email(request.form["email"].strip().lower())
    if not user or not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Credenciales inválidas.", "login_error")
        return redirect("/")

    session["user_id"] = user.id
    session["user_name"] = user.first_name
    return redirect("/libros")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")