from flask import render_template, request, redirect, session, flash
from app import app
from app.models.pelicula import Pelicula
from app.models.usuario import Usuario
from app.models.comentario import Comentario

@app.route('/cine')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')
    
    usuario = Usuario.get_by_id({"id": session['usuario_id']})
    peliculas = Pelicula.get_all()
    return render_template('dashboard.html', usuario=usuario, peliculas=peliculas)

@app.route('/cine/nueva')
def nueva_pelicula():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nueva_pelicula.html')

@app.route('/cine/crear', methods=['POST'])
def crear_pelicula():
    if 'usuario_id' not in session:
        return redirect('/')
    
    session['pelicula_form'] = request.form
    if not Pelicula.validar_pelicula(request.form):
        return redirect('/cine/nueva')
    
    data = {
        "titulo": request.form['titulo'],
        "director": request.form['director'],
        "fecha_estreno": request.form['fecha_estreno'],
        "sinopsis": request.form['sinopsis'],
        "usuario_id": session['usuario_id']
    }
    Pelicula.save(data)
    session.pop('pelicula_form', None)
    return redirect('/cine')

@app.route('/cine/<int:id>')
def ver_pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    pelicula = Pelicula.get_by_id({"id": id})
    if not pelicula:
        return redirect('/cine')
    
    comentarios = Comentario.get_by_pelicula({"pelicula_id": id})
    return render_template('pelicula_info.html', pelicula=pelicula, comentarios=comentarios)

@app.route('/cine/editar/<int:id>')
def editar_pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    pelicula = Pelicula.get_by_id({"id": id})
    if not pelicula or pelicula.usuario_id != session['usuario_id']:
        return redirect('/cine')
    
    return render_template('editar_pelicula.html', pelicula=pelicula)

@app.route('/cine/actualizar/<int:id>', methods=['POST'])
def actualizar_pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    pelicula = Pelicula.get_by_id({"id": id})
    if not pelicula or pelicula.usuario_id != session['usuario_id']:
        return redirect('/cine')
    
    session['pelicula_form'] = request.form
    if not Pelicula.validar_pelicula(request.form, pelicula_id=id):
        return redirect(f'/cine/editar/{id}')
    
    data = {
        "id": id,
        "titulo": request.form['titulo'],
        "director": request.form['director'],
        "fecha_estreno": request.form['fecha_estreno'],
        "sinopsis": request.form['sinopsis']
    }
    Pelicula.update(data)
    session.pop('pelicula_form', None)
    return redirect('/cine')

@app.route('/cine/eliminar/<int:id>')
def eliminar_pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    pelicula = Pelicula.get_by_id({"id": id})
    if pelicula and pelicula.usuario_id == session['usuario_id']:
        Pelicula.destroy({"id": id})
    return redirect('/cine')

# Rutas para el BONUS de Comentarios
@app.route('/cine/comentario/crear', methods=['POST'])
def crear_comentario():
    if 'usuario_id' not in session:
        return redirect('/')
    
    pelicula_id = request.form['pelicula_id']
    pelicula = Pelicula.get_by_id({"id": pelicula_id})
    
    # BONUS: Un usuario no puede comentar su propia película
    if pelicula and pelicula.usuario_id == session['usuario_id']:
        flash("No puedes comentar en tu propia película.", "comentario")
        return redirect(f'/cine/{pelicula_id}')
    
    if request.form.get('contenido', '').strip():
        data = {
            "contenido": request.form['contenido'],
            "usuario_id": session['usuario_id'],
            "pelicula_id": pelicula_id
        }
        Comentario.save(data)
    return redirect(f'/cine/{pelicula_id}')

@app.route('/cine/comentario/eliminar/<int:id>')
def eliminar_comentario(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    comentario = Comentario.get_by_id({"id": id})
    if comentario and comentario.usuario_id == session['usuario_id']:
        Comentario.destroy({"id": id})
        return redirect(f'/cine/{comentario.pelicula_id}')
    return redirect('/cine')