#Pasar argumentos
#Para poder personalizar nuestras instancia vamos a pasar algunos 
# argumentos al método __init__ y que de esta manera podamos asignarle 
# a los atributos los valores correspondientes.
class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

#Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 100000, 20000)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 20000, 0)
catalina = Usuario("Catalina", "Acosta", "catalina01acost@gmail.com", 500000, 0)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido)
print(daniel.email)
print(daniel.limite_credito)
print(daniel.saldo_pagar)

print(catalina.nombre) #Imprime: Catalina
print(catalina.apellido)
print(catalina.email)
print(catalina.limite_credito)
print(catalina.saldo_pagar)

#-----------------------------------------------------------
#--- Tarea Rápida
"""
-Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
-Crear 3 instancias para la clase con distintos estudiantes.
-Imprime el nombre y apellido concatenado + especialidad
"""

class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

jest = Estudiante("28.979.420-9", "Jest", "Terss", "Recursos Humanos", "29/09/1965")
rotie = Estudiante("48.284.289-4", "Rotie", "Pote", "Logistica", "18/05/1990")
hart = Estudiante("19.394.209-1", "Hart", "Luit", "Programación", "26/05/2000")

print(f"mi nombre es {jest.nombre}, mi apellido es {jest.apellido} y pertenesco a la especialidad de {jest.especialidad}")
print(f"mi nombre es {rotie.nombre}, mi apellido es {rotie.apellido} y pertenesco a la especialidad de {rotie.especialidad}")
print(f"mi nombre es {hart.nombre}, mi apellido es {hart.apellido} y pertenesco a la especialidad de {hart.especialidad}")
