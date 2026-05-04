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