# Métodos de clase y estáticos
# Atributos, métodos de clases y métodos estáticos.

#DEFINICION DE LA CLASE
class Estudiante:
    #Atributo de la clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes
    estudiantes = []

#Método CONTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota
        

        #Agregar elementos a lista Estudiante (objeto)
        Estudiante.estudiantes.append(self)

#Método de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

#Método de clase
#Usa "CLS" porque trabaja con la informacion de la clase.
    @classmethod
    def cambiarColegio(cls, new_name):
        cls.colegio = new_name

    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)

#Método estatico
#Este no usa CLS ni SELF, solo parametros.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False

#Creacion de objetos
e1 = Estudiante("Koi", 4.0)
e2 = Estudiante("Nomi", 6.0)
e3 = Estudiante("Kai", 1.0)

#Uso de métodos de instancia
print("== MÉTODOS DE INSTANCIA ==")
#Mostrar datos de estudiantes.
e1.mostrar_info()
print()
e2.mostrar_info()
print()
e3.mostrar_info()
print()

#Usar atributo de clase
print("=== ATRIBUTO DE CLASES ===")
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

#Uso de Método de clase
print("=== MÉTODO DE CLASES ===")
Estudiante.cambiarColegio("Purkuyen")
e1.colegio = "VVH"
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

#Contar estudiantes
print("=== CONTAR ESTUDIANTES ===")
print(f"Total de estudiantes: {Estudiante.cantidad_estudiantes()}")

#Método estatico
print("=== MÉTODO ESTATICO ===")
print(f"¿{e1.nombre} Aprueba?")
print(Estudiante.aprobar(e1.nota))

print(f"¿{e2.nombre} Aprueba?")
print(Estudiante.aprobar(e2.nota))

print(f"¿{e3.nombre} Aprueba?")
print(Estudiante.aprobar(e3.nota))


#----------------------------------------------------------------------------------

## Función repaso.
## Crear una función que valide usuario y contraseña

def validador(user, password):
    if user == "Player" and password == "I See You":
        print(f"Bien! Yo, Jester, te doy la bienvenido al show, {user}")
        return True
    else:
        print("Lo siento pero Jester no recuerda haberte invitado")
        return False

def enviarDatos():
    print("Hola a todos los espectadores! veo un nuevo invitado!")
    username = input("Y dime, tu nombre es? ")
    password = input("Dime la contraseña ")
    validador(username, password)

enviarDatos()