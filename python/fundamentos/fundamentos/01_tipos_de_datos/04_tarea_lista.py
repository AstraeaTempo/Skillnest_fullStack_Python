'''Actividad: Gestor de inventario'''

'''1.- Creación: Crear una lista llamada "inventario" que contenga los siguientes. 
Articulos: "laptop", "ratón", "monitor", "cable hdmi"'''

inventario = ['laptop', 'raton', 'monitor', 'cable hdmi']

'''2.- Expansión: Utiliza el método correspondiente para agregar "impresora"
y "teclado" al final de la lista.'''

inventario.append("impresora")
inventario.append("teclado")
print(inventario)

'''3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos 
totales hay en la lista.'''

print(len(inventario))

'''4.- Acceso y modificación: Modifica "teclado" por "teclado mecánico'''

inventario[5] = "teclado mecanico"
print(inventario) #lo puse solo para que se vea que si se cambio

'''5.- Slicing: Crear una nueva lista llamada "promoción", debe contener
solo los 3 primeros elementos de la lista "inventario".'''

promocion = inventario
print(promocion[:3])

'''6.- Mostrar la lista de inventario ordenado alfabeticamente.'''

inventario.sort()
print(inventario)

'''7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento
eliminado y la lista final.'''

inventario.pop()
print(inventario)