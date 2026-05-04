#Crear una función que reciba una lista de edades y clasifique a las
#personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
#Debe mostrar la cantidad de personas en cada grupo.

print("Primera forma")
def edades_1(lista):
    num1 = 0
    for i in range(len(lista)):
        if lista[i] >= 60:
            num1 += 1
    return num1
def edades_2(lista):
    num2 = 0
    for i in range(len(lista)):
        if 18 <= lista[i] <= 59:
            num2 += 1
    return num2
def edades_3(lista):
    num3 = 0
    for i in range(len(lista)):
        if lista[i] <= 17:
            num3 += 1
    return num3

def gente():
    edad = []
    inp = int(input("Cuantas personas van a ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">> "))
        if var !="":
            edad.append(var)
        else:
            print("Ingrese valor valido...")
    resultado_1 = edades_1(edad)
    print(f"Hay {resultado_1} adultos mayores")
    resultado_2 = edades_2(edad)
    print(f"Hay {resultado_2} adultos")
    resultado_3 = edades_3(edad)
    print(f"Hay {resultado_3} menores de edad")
gente()

#------------------------------------------------------------------------------------------------------

print("Segunda forma")
def edades(lista):
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(len(lista)):
        if 0 <= lista[i] <= 17:
            num1 += 1
        elif 18 <= lista[i] <= 59:
            num2 += 1
        else:
            num3 += 1
    print(f"hay {num1} menores de edad, {num2} adultos y {num3} adultos mayores")

def gente():
    edad = []
    inp = int(input("Cuantas personas van a ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">> "))
        if var !="":
            edad.append(var)
        else:
            print("Ingrese valor valido...")
    resultado = edades(edad)
gente()