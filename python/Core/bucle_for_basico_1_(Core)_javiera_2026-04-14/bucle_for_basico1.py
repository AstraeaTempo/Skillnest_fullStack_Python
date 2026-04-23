"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

for gen_niv in range (0,101):
    print(gen_niv)

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

for potencia in range(2, 502, 2):
    print(potencia)

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

for mojis in range(1, 101):
    if mojis % 10 == 0:
        print(":P")
    elif mojis % 5 == 0:
        print(":D")
    else:
        print(mojis)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

result = 0
for suma_num in range(0, 500000, 2):
    result += suma_num

print(result)

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

for tiempo in range(2024, -3, -3):
    print(tiempo)

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)
# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

inicio = 4
fin = 20
salto = 3
for i in range(inicio, fin, 3):
    if i % salto:
        print(i)