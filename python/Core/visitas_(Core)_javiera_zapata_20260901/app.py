from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# Es necesario definir una clave secreta para manejar sesiones en Flask
app.secret_key = 'clave_secreta_super_segura'


@app.route('/')
def inicio():
    # Inicialización de variables en sesión si no existen
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1

    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template('index.html',
                           visitas=session['visitas'],
                           reinicios=session['reinicios'])


@app.route('/sumar_dos', methods=['POST'])
def sumar_dos():
    # Suma 2 a las visitas (se compensa el +1 que ocurre automáticamente al redirigir a '/')
    if 'visitas' in session:
        session['visitas'] += 1
    return redirect('/')


@app.route('/incrementar_personalizado', methods=['POST'])
def incrementar_personalizado():
    # Obtiene el valor del formulario y le resta 1 para compensar el incremento al redirigir
    cantidad = request.form.get('cantidad', type=int)
    if cantidad and 'visitas' in session:
        session['visitas'] += (cantidad - 1)
    return redirect('/')


@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    # Reinicia el contador de visitas y suma 1 al contador de reinicios
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1

    # Establecemos en -1 para que al redirigir a '/' sume 1 y quede en 0
    session['visitas'] = -1
    return redirect('/')


@app.route('/destruir_sesion')
def destruir_sesion():
    # Elimina completamente la sesión
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)