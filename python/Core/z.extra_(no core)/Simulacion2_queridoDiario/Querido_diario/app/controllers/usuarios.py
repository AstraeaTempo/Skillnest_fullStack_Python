from app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from app.models.usuario import Usuario

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    password_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "edad": request.form['edad'],
        "password": password_hash
    }
    usuario_id = Usuario.save(data)
    session['usuario_id'] = usuario_id
    session['nombre'] = request.form['nombre']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    usuario_db = Usuario.get_by_email({"email": request.form['email']})
    if not usuario_db:
        flash("El email no se encuentra registrado.", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(usuario_db.password, request.form['password']):
        flash("Contraseña incorrecta.", "login")
        return redirect('/')

    session['usuario_id'] = usuario_db.id
    session['nombre'] = usuario_db.nombre
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')