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
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado
def mostrar():
    nombres = []
    cantidad = int(input("¿cuantos nombres quiere ingresar?: "))
    for i in range(cantidad):
        nombre = input("ingrese un nombre: ")
        print(f"{nombre} agregado con exito a la lista")
        nombres.append(nombre)
    
    listaNombres = filtrar(nombres)
    print(f"los nombres con mas de 5 letras son: \n- {("\n").join(listaNombres)}")

mostrar()

#Ejercicio 4-------------------------------------------------------------------------------------------

def listaNotas(notas):
    lista = 0
    promedio = 0
    for i in range(len(notas)):
        lista += notas[1]
        promedio = lista / (len(notas) + 1)

    if notas[i] >= 4.0 and notas[i] <= 7.0:
        print(f"el estudiante aprueba con {promedio}")
    elif notas[i] >= 1 and notas[i] <= 3.9:
        print(f"el estudiante no aprueba con {promedio}")
    else:
        return "error"

def notis():
    largo = int(input("Cuantas notas va a ingresar: "))
    nota = []
    for i in range(largo):
        inp = float(input(f"Ingresa nota {i + 1}: "))
        if inp != "":
            nota.append(inp)
    print(listaNotas(nota))
notis()

#Ejercicio 5-------------------------------------------------------------------------------------------

def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: \n{precioInicial}\ny con descuento \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese cantidad de productos: "))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor del producto:\n"))
        listaPrecios.append(valorProducto)
    descuento(listaPrecios)
valores()

#Ejercicio 6-------------------------------------------------------------------------------------------

def par_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    elif numero % 3 == 0:
        print(f"El número {numero} es Impar.")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingrese un número: "))
    par_impar(num)
recibirNum()

#Ejercicio 7-------------------------------------------------------------------------------------------



#Ejercicio 8-------------------------------------------------------------------------------------------



#Ejercicio 9-------------------------------------------------------------------------------------------



#Ejercicio 10------------------------------------------------------------------------------------------



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
        ()
    elif opcion == "2":
        print("\n--------- Cadenas de Vocales ---------")
        ()
    elif opcion == "3":
        print("\n--------- Nombres con más de 5 letras ---------")
        mostrar()
    elif opcion == "4":
        print("\n--------- Notas: Apruebas o Repruebas ---------")
        notis()
    elif opcion == "5":
        print("\n--------- Descuento del 10% ---------")
        valores()
    elif opcion == "6":
        print("\n--------- Par o Impar ---------")
        recibirNum()
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
        print("saliendo...")
        continuar = False
    else:
        print("opcion no valida, intenta otra vez")