#💻 Código base 
class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        self.lista_reproduccion(titulo)
        print(f"Titulo '{titulo}' agregado correctamente")


    def ver_contenido(self, titulo):
        if titulo in self.lista_reproduccion:
            print(f"El usuario {self.nombre} esta viendo '{titulo}'")
        else:
            print(f"Titulo no encontrado {titulo}")


    def cambiar_suscripcion(self, nueva_suscripcion):
        susAntigua = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f"Suscripción cambia de {susAntigua} a {nueva_suscripcion}")


    def mostrar_info_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        if len(self.lista_reproduccion) == 0:
            print(f"La lista de reproducción esta vacia")
        else:
            print(f"Lista de reproducción: \n- {"\n- ".join(self.lista_reproduccion)}")

# Todos los valores que se deban registrar debe ser con input
# Añadir un menu While para llamar a los métodos.
# (Menú de selección)

miyano = UsuarioStreaming("Miyano", "miyano@codingdojo.la")
miyano.agregar_a_lista("La vida")
miyano.cambiar_suscripcion("Premium")
miyano.ver_contenido("ORV")
miyano.mostrar_info_usuario()

sasaki = UsuarioStreaming("Sasaki", "sasaki@codingdojo.la")
sasaki.agregar_a_lista("Tu vida")
sasaki.cambiar_suscripcion("Estandar")
sasaki.ver_contenido("Hablame")
sasaki.mostrar_info_usuario()

#Menu
continuar = True
while continuar:
    print("\n---ejercicios python---")
    print("---1.- ejercicio 1---")
    print("---2.- ejercicio 2---")
    print("---3.- ejercicio 3---")
    print("---4.- ejercicio 4---")
    opcion = input("\n---- elige una opcion: (1-4) (0 para salir) = ")
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
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no visible, intenta otra vez")