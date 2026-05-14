#Crear una función que reciba una lista de edades y clasifique a las
#personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
#Debe mostrar la cantidad de personas en cada grupo.

print("Final")
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


#Menu While
continuar = True
while continuar:
    print("\n---ejercicios python---")
    print("---6.- ejercicio 6---")
    opcion = input("\n---- elige una opcion: (1-1) (0 para salir) = ")
    if opcion == "6":
        print("\n--------- Edades ---------")
        gente()
    elif opcion == "0":
        print("saliendo...")
        continuar = False
    else:
        print("opcion no valida, intenta otra vez")

        #wuju bru




import os
def limpiarConsola():
    os.system('cls')



# Arael Anabalón
"""
7. Crear una función que reciba una lista de números y determine si todos los números son positivos.
Si encuentra al menos un número negativo, debe indicarlo y detener el recorrido.
"""
def verificarPositivos(nums):
    for i in range(len(nums)):
        negativoEncontrado = False
        if nums[i] < 0:
            print(f"El número {nums[i]} es negativo!\nDeteniendo el recorrido...")
            negativoEncontrado = True
            break
    if not negativoEncontrado:
        print(f"Todos los números ingresados son positivos!\nNúmeros ingresados:\n{nums}")
    
def recibirNums():
    cantidad = int(input("Cantidad de números que ingresará: "))
    listaNums = []
    for i in range(cantidad):
        num = int(input(f"{i + 1}. "))
        listaNums.append(num)
    verificarPositivos(listaNums)



# Javiera Zapata
"""
6. Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
Debe mostrar la cantidad de personas en cada grupo.
"""
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



# Daniel Jiménez
"""
Crear una función que reciba una lista de números y determine cuál es el número que más se repite.
Debe mostrar el número y la cantidad de veces que aparece.
"""
def numeroRepetido(numN):
    # Creamos un diccionario para contar las ocurrencias
    contador = {}
    for num in numN:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    # Buscamos el número que más se repite
    max_repetido = max(contador, key=contador.get)
    veces_repetidas = contador[max_repetido]
    print(f"El número {max_repetido} es el que más se repite, apareciendo {veces_repetidas} veces.")

def recibirNumero():
    cantidad = int(input("Cantidad de números a colocar: "))
    listaNumero = []
    for i in range(cantidad):
        num = int(input(f"{i + 1}. "))
        listaNumero.append(num)
    numeroRepetido(listaNumero)

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print("\n--- Ejercicios Python ---")
    print("--- 1. Arael Anabalón ---")
    print("--- 2. Javiera Zapata ---")
    print("--- 3. Daniel Jiménez ---")
    opcion = input("\n---Elije una opción: (1-3) (0 para salir): ")
    if opcion == "1":
        limpiar_consola()
        print("\nEjercicio 7 (Por Arael.A): ")
        
    elif opcion == "2":
        limpiar_consola()
        print("\nEjercicio 6 (Por Javiera.A): ")
        
    elif opcion == "3":
        limpiar_consola()
        print("\nEjercicio 4 (Por Daniel.J): ")
        
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")