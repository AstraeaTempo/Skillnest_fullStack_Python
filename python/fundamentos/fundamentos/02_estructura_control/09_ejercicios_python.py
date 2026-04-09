#Guía de Ejercicios: Lógica Fundamental

#I. Interacción y Condicionales (Básico)
#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
# El programa debe imprimir los primeros $n$ números pares positivos.

n = int(input("¿Cuántos números pares deseas ver?: "))
# Usamos un rango que empiece en 2, llegue hasta n*2 + 1 y salte de 2 en 2
for i in range(1, n+2):
    resultado = i*2
    print(resultado)

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor 
# de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.

from datetime import date
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
anio_actual = date.today().year # Obtenemos el año actual del sistema
edad = anio_actual - anio_nacimiento

if edad >= 18:
    print(f"Tienes {edad} años. Eres mayor de edad.")
else:
    faltan = 18 - edad
    print(f"Tienes {edad} años. Te faltan {faltan} años para la mayoría de edad.")

#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera 
# los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.

precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad comprada: "))
subtotal = precio * cantidad

if subtotal > 100:
    descuento = subtotal * 0.15 # Calculamos el 15%
    total = subtotal - descuento
else:
    descuento = 0
    total = subtotal

print(f"Subtotal: ${subtotal} | Descuento: ${descuento} | Total: ${total}")

#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, 
# Negativo-Par, Negativo-Impar o Cero.

num = int(input("Ingresa un número: "))

if num == 0:
    print("Cero")
elif num > 0:
    # Anidamos la lógica para ver si es par o impar
    tipo = "Par" if num % 2 == 0 else "Impar"
    print(f"Positivo-{tipo}")
else:
    tipo = "Par" if num % 2 == 0 else "Impar"
    print(f"Negativo-{tipo}")

#II. Iteraciones y Bucles (Intermedio)

#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
# pero solo muestra los resultados que sean múltiplos de 3.

num = int(input("Ingresa un número para su tabla: "))

for i in range(1, 13):
    resultado = num * i
    # Verificamos si el resultado es múltiplo de 3 usando el operador módulo %
    if resultado % 3 == 0:
        print(f"{num} x {i} = {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe 
# terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total 
# (sin incluir el negativo).

suma_total = 0
# Usamos un bucle infinito que romperemos con 'break'
while True:
    n = float(input("Ingresa un número (negativo para salir): "))
    if n < 0:
        break # Detiene el bucle inmediatamente
    suma_total += n

print(f"La suma total es: {suma_total}")

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la 
# cadena y contar cuántas vocales tiene en total.

frase = input("Ingresa una frase: ").lower() # Convertimos a minúsculas para facilitar la cuenta
vocales = "aeiou"
contador = 0

for caracter in frase:
    if caracter in vocales:
        contador += 1

print(f"Total de vocales: {contador}")

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
# Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.

password_correcta = "python123"
# El rango define los 3 intentos
for intento in range(1, 4):
    entrada = input(f"Intento {intento} - Ingresa la contraseña: ")
    if entrada == password_correcta:
        print("Acceso concedido.")
        break
else:
    # El 'else' de un 'for' se ejecuta si el bucle termina sin un 'break'
    print("Acceso bloqueado. Agotaste los intentos.")

#III. Manejo de Arreglos / Listas (Avanzado)

#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en 
# el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

nombres = []
for i in range(5):
    nom = input(f"Ingrese nombre {i+1}: ")
    nombres.append(nom)

# Invertimos la lista y la recorremos
print("\nNombres en orden inverso:")
for n in reversed(nombres):
    print(n)

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
# Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

cantidad = int(input("¿Cuántas notas vas a ingresar? "))
notas = []

for i in range(cantidad):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

# Calculamos estadísticas básicas
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga 
# solo los números que sean mayores a 50. Muestra ambos arreglos.

numeros = [10, 55, 23, 89, 45, 72, 50, 100] # Ejemplo de entrada
mayores_50 = []

for n in numeros:
    if n > 50:
        mayores_50.append(n)

print(f"Original: {numeros}")
print(f"Filtrados (>50): {mayores_50}")

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de 
# una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué 
# índice (posición) está.

ciudades = ["Tokio", "París", "Santiago", "Madrid", "Bogotá", "Lima", "Oslo", "Seúl", "Roma", "Berlín"]
busqueda = input("Ciudad a buscar: ")

encontrado = False
for i in range(len(ciudades)):
    if ciudades[i].lower() == busqueda.lower():
        print(f"¡Encontrada! {busqueda} está en el índice {i}.")
        encontrado = True
        break

if not encontrado:
    print("La ciudad no está en la lista.")

#IV. Retos de Lógica Combinada

#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. 
# Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: 
# Producto: [Nombre] - Precio: $[Valor].

nombres_productos = []
precios = []

for i in range(3):
    nom = input(f"Nombre del producto {i+1}: ")
    pre = float(input(f"Precio de {nom}: "))
    nombres_productos.append(nom)
    precios.append(pre)

print("\n--- INVENTARIO ---")
# Usamos range para acceder a ambos arreglos por el mismo índice
for i in range(len(nombres_productos)):
    print(f"Producto: {nombres_productos[i]} - Precio: ${precios[i]}")

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a 
# una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final,
#  muestra la lista ordenada alfabéticamente.

lista = []
while True:
    item = input("Agregue un artículo (o escriba 'terminar'): ")
    if item.lower() == "terminar":
        break
    lista.append(item)

lista.sort() # Orden alfabético
print("\nLista de Compras:")
for item in lista:
    print(f"- {item}")

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

temperaturas = []
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Llenado del arreglo
for i in range(7):
    temp = float(input(f"Temp. del {dias[i]}: "))
    temperaturas.append(temp)

# Procesamiento
promedio = sum(temperaturas) / 7
dias_calurosos = 0
min_temp = temperaturas[0]
dia_mas_frio = dias[0]

for i in range(7):
    # Contar días > 25
    if temperaturas[i] > 25:
        dias_calurosos += 1
    # Buscar el más bajo manualmente
    if temperaturas[i] < min_temp:
        min_temp = temperaturas[i]
        dia_mas_frio = dias[i]

print(f"\nPromedio semanal: {promedio:.1f}°C")
print(f"Días con más de 25°C: {dias_calurosos}")
print(f"Día más frío: {dia_mas_frio} con {min_temp}°C")