from app import app
from flask import render_template, redirect, request, session, flash
from app.models.entrada import Entrada
from app.models.usuario import Usuario

@app.route('/dashboard')
def dashboard():
    # Seguridad: Verificación de sesión[cite: 2]
    if 'usuario_id' not in session:
        return redirect('/')

    usuario = Usuario.get_by_id({"id": session['usuario_id']})
    entradas = Entrada.get_by_user({"usuario_id": session['usuario_id']})
    return render_template('dashboard.html', usuario=usuario, entradas=entradas)

@app.route('/nueva')
def vista_nueva_entrada():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nueva_entrada.html')

@app.route('/nueva/crear', methods=['POST'])
def crear_entrada():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Entrada.validar_entrada(request.form):
        return redirect('/nueva')

    data = {
        "fecha_entrada": request.form['fecha_entrada'],
        "notas": request.form['notas'],
        "usuario_id": session['usuario_id']
    }
    Entrada.save(data)
    return redirect('/dashboard')

@app.route('/ver/<int:id>')
def ver_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')

    entrada = Entrada.get_by_id({"id": id})
    # Seguridad: Asegurar que el usuario no vea entradas de otros[cite: 2]
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')

    return render_template('ver_entrada.html', entrada=entrada)

@app.route('/editar/<int:id>')
def vista_editar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')

    entrada = Entrada.get_by_id({"id": id})
    # Seguridad: Asegurar que el usuario no edite entradas de otros[cite: 2]
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')

    return render_template('editar_entrada.html', entrada=entrada)

@app.route('/editar/actualizar/<int:id>', methods=['POST'])
def actualizar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')

    entrada = Entrada.get_by_id({"id": id})
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')

    if not Entrada.validar_entrada(request.form):
        return redirect(f'/editar/{id}')

    data = {
        "id": id,
        "fecha_entrada": request.form['fecha_entrada'],
        "notas": request.form['notas']
    }
    Entrada.update(data)
    return redirect('/dashboard')

@app.route('/borrar/<int:id>')
def borrar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')

    entrada = Entrada.get_by_id({"id": id})
    # Seguridad: Asegurar que el usuario NO pueda borrar entradas ajenas[cite: 2]
    if entrada and entrada.usuario_id == session['usuario_id']:
        Entrada.delete({"id": id})

    return redirect('/dashboard')

@app.route('/buscar')
def buscar_entrada():
    if 'usuario_id' not in session:
        return redirect('/')

    termino = request.args.get('q', '')
    data = {
        "usuario_id": session['usuario_id'],
        "termino": f"%{termino}%"
    }
    resultados = Entrada.search_by_notes(data)
    return render_template('buscar_entrada.html', entradas=resultados, termino=termino)