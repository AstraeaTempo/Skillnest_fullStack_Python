# *Objetivo*
Practicar el uso de sesión para guardar información del usuario
Comprobar la existencia de sesión
Practicar la inicialización de sesión
Practicar la edición de información en sesión

 ¿Por qué es importante?
Muchos sitios web, como enciclopedias digitales o catálogos de videojuegos, manejan datos estructurados que pueden consultarse por ID o nombre. Esta práctica te ayudará a entender cómo crear rutas dinámicas en Flask, usar bucles en plantillas, manejar archivos estáticos y enviar datos mediante diccionarios.

# *Instrucciones*
Para esta asignación estaremos creando una aplicación que cuente la cantidad de veces que has visitado una página, parecido a la funcionalidad que tienen algunos sitios web.

## Nivel 1

* En la ruta raíz (http://127.0.0.1:5000/) muestra la cantidad de veces que el cliente ha visitado el sitio.

* Crea también una ruta (http://127.0.0.1:5000/destruir_sesion) que elimina la sesión y redirija a la ruta principal.

## Nivel 2

Agrega un botón que al hacer click te aumenta la cantidad visitada +2
Agrega un botón para reiniciar a 0 la cantidad de visitas por el cliente

## Nivel 3

Agrega un formulario que permita ingresar un número y que aumente esa cantidad al número de visitas
Cuantifica la cantidad de veces que se a reiniciado el contador de visitas y muéstralo en la ruta principal
 **Comprobar la sesión**

Ten en cuenta que para poder hacer esta asignación será necesario comprobar si existe o no la sesión. Eso lo hacemos de la siguiente manera:

# *if 'nombre_de_propiedad' in session:*
       print("Existe esa propiedad en sesión")
# *else:*
       print("No existe la propiedad")

**Eliminar la sesión:**
Para eliminar algún dato almacenado en sesión, lo hacemos de la siguiente manera:

session.clear() #Elimina todas las propiedades de sesión
session.pop('nombre_de_propiedad') #Elimina una propiedad específica

* Crea un nuevo proyecto de Flask llamado visitas

* Crea la ruta principal, donde muestre la cantidad de visitas que el cliente ha hecho a la página

* Actualiza múltiples veces para comprobar el funcionamiento de las visitas

* Crea la ruta /destruir_sesion que elimine la sesión y redirige a la ruta raíz.

* BONUS DE PLATA: Agrega un botón para agregar la cantidad de visitas en 2

* BONUS DE PLATA: Agrega un botón para reiniciar la cantidad de visitas

* BONUS DE ORO: Agrega un formulario que permita ingresar un número y que aumente en esa cantidad las visitas

* BONUS DE ORO: Muestra la cantidad de veces que la cantidad de visitas ha sido reiniciado

*Nota: Te recomendamos tener en cuenta que por temas de seguridad el sistema no permite carga de archivos .py directamente, por lo tanto, te sugerimos agregar el link de GitHub con la tarea o si deseas adjuntar el archivo comprimido*