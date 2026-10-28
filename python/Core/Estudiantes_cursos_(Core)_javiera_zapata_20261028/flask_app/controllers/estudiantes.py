from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


@app.route("/estudiantes/nuevo")
def nuevo_estudiante():
    cursos = Curso.get_all()

    return render_template(
        "nuevo_estudiante.html",
        cursos=cursos
    )


@app.route("/estudiantes/crear", methods=["POST"])
def crear_estudiante():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad = request.form.get("edad", "").strip()
    curso_id = request.form.get("curso_id", "").strip()

    if (
        not nombre
        or not apellido
        or len(nombre) > 45
        or len(apellido) > 45
        or not edad.isdigit()
        or not curso_id.isdigit()
    ):
        return redirect(url_for("nuevo_estudiante"))

    edad = int(edad)
    curso_id = int(curso_id)

    if edad < 1 or Curso.get_curso_con_estudiantes(curso_id) is None:
        return redirect(url_for("nuevo_estudiante"))

    resultado = Estudiante.save({
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "curso_id": curso_id
    })

    if resultado is False:
        return redirect(url_for("nuevo_estudiante"))

    return redirect(url_for("cursos"))