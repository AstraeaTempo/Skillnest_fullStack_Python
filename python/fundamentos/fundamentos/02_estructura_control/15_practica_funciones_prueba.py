#Practica para la prueba.
'''
Ejercicios a desarrollar
Su programa deberá considerar las siguientes funciones:

1. Crear una función que reciba una lista de números enteros y muestre 
cuál es el número mayor y cuál es el menor.

2. Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.

3. Crear una función que reciba una lista de nombres y muestre 
únicamente aquellos que tengan más de 5 letras.

4. Crear una función que reciba una lista de notas (números decimales), calcule el promedio e 
indique si el estudiante aprueba (promedio mayor o igual a 4.0).

5. Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, 
mostrando el valor original y el nuevo valor.

6. Crear una función que reciba un número entero y determine si es par o impar.

7. Crear una función que reciba una lista de edades y muestre cuántas personas son 
mayores de edad (18 años o más).

8. Crear una función que reciba una lista de palabras y permita buscar cuántas veces 
aparece una palabra específica ingresada por el usuario.

9. Crear una función que reciba una lista de números y genere una nueva lista que contenga
únicamente los números positivos.

10. Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) 
y muestre cuáles tienen un stock menor a 5 unidades.
'''

#Ejercicio 1-------------------------------------------------------------------------------------------
def numMayorAndMenor(listado):
    listaNum = listado
    menor = min(listaNum)
    mayor = max(listaNum)
    print(f"El número menor es: {menor}\nEl número mayor es: {mayor}")
def recibirLista():
    limit = int (input("Ingresa el limite de valor: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = input(f"Ingrese un número entero {i} de {limit}: ")
        listadoNum.append(num)
        i += 1
    numMayorAndMenor(listadoNum)

#Ejercicio 2-------------------------------------------------------------------------------------------

def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales
def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales.")
def vocal():
    texto = input("Ingrese una cadena de texto: ")
    contar_vocales(texto)

#Ejercicio 3-------------------------------------------------------------------------------------------

def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) >5:
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    nombreLargos = []
    cantidad = int(input("¿Cuántos nombres quiere ingresar?: "))
    for i in range(cantidad):
        nombre = input("Ingrese un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombres)
    for nombre in filtrar(nombres):
        nombreLargos.append(nombre)
    print(f"Los nombres con más de 5 letras son: ")
mostrar()

#Ejercicio 4-------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

#Ejercicio 5-------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

#Ejercicio 6-------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

#Ejercicio 7-------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

#Ejercicio 8-------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

#Ejercicio 9-------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

#Ejercicio 10------------------------------------------------------------------------------------------

def t():
    pass

def t():
    pass

# Requisitos obligatorios Su trabajo debe cumplir con lo siguiente:

#Uso de funciones con parámetros
#Uso de menú con ciclo while
#Uso de input() para solicitar datos
#Uso de listas (arreglos)
#Uso de diccionarios
#Uso de ciclos for
#Uso de estructuras condicionales (if, elif, else)
#Código ordenado, comentado y correctamente indentado
#Opción de salida del programa (0. Salir)

#Menu
continuar = True
while continuar:
    print("\n---ejercicios python---")
    print("---1.- ejercicio 1---")
    print("---2.- ejercicio 2---")
    print("---3.- ejercicio 3---")
    print("---4.- ejercicio 4---")
    print("---5.- ejercicio 5---")
    print("---6.- ejercicio 6---")
    print("---7.- ejercicio 7---")
    print("---8.- ejercicio 8---")
    print("---9.- ejercicio 9---")
    print("---10.- ejercicio 10---")
    opcion = input("\n---- elige una opcion: (1-10) (0 para salir) = ")
    if opcion == "1":
        print("\n--------- Número mayor y menor ---------")
        recibirLista()
    elif opcion == "2":
        print("\n--------- Cadenas de Vocales ---------")
        vocal()
    elif opcion == "3":
        print("\n--------- Nombres con más de 5 letras ---------")
        mostrar()
    elif opcion == "4":
        print("\n--------- Notas: Apruebas o Repruebas ---------")
        ()
    elif opcion == "5":
        print("\n--------- Descuento del 10% ---------")
        ()
    elif opcion == "6":
        print("\n--------- Par o Impar ---------")
        ()
    elif opcion == "7":
        print("\n--------- Mayor de 18 años ---------")
        ()
    elif opcion == "8":
        print("\n--------- Palabra específica ---------")
        ()
    elif opcion == "9":
        print("\n--------- Lista con números positivos ---------")
        ()
    elif opcion == "10":
        print("\n--------- Productos con stock menor a 5 ---------")
        ()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no visible, intenta otra vez")