#💻 Código base 
class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion += titulo


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        self.nombre += titulo


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        self.suscripcion += nueva_suscripcion


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        usuario += self

miyano = UsuarioStreaming("Miyano", "miyagi@codingdojo.la", "Gratis")
sasaki = UsuarioStreaming("Sasaki", "daniel@codingdojo.la", "Premium")

# Todos los valores que se deban registrar debe ser con input
# Añadir un menu While para llamar a los métodos.
# (Menú de selección)

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
        print("\nEjecutando ejercicio 1: ")
        ()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        ()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        ()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        ()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        ()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        ()
    elif opcion == "7":
        print("\nEjecutando ejercicio 7: ")
        ()
    elif opcion == "8":
        print("\nEjecutando ejercicio 8: ")
        ()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9: ")
        ()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10: ")
        ()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no visible, intenta otra vez")