from flask import render_template, request, redirect, session, flash
from app import app
from app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/cine')
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    session['registro_form'] = request.form
    if not Usuario.validar_registro(request.form):
        return redirect('/')
    
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": password_hash
    }
    usuario_id = Usuario.save(data)
    session['usuario_id'] = usuario_id
    session.pop('registro_form', None)
    return redirect('/cine')

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.get_by_email({"email": request.form['email']})
    if not usuario:
        flash("El email debe estar registrado en BD.", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("La contraseña debe ser la correspondiente a la BD.", "login")
        return redirect('/')
    
    session['usuario_id'] = usuario.id
    return redirect('/cine')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')