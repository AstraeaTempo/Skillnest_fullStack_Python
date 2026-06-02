class Usuario:
    usuarios = []
    
    def __init__(self, username, email, password, tipo_usuario):
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario
        Usuario.usuarios.append(self.username)

    def info_user (self):
        print(f"Nombre: {self.username}")
        print(f"Gmail: {self.email}")
        print(f"Password: {self.password_hash}")
        print(f"Tipo usuario: {self.tipo_usuario}")

#------------------------------------------------------------------------------------------------------

class Pedido:
    pedidos = []

    def __init__(self, usuario):
        self.usuario = usuario
        Pedido.pedidos.append(self.usuario)

        def pedidos_realizados():
            pass #por mientras

#------------------------------------------------------------------------------------------------------

class Pelicula:
    peliculas = []
    
    def __init__(self, titulo, anio, estado_restauracion, precio_unitario, stock, formato):
        self.titulo = titulo
        self.anio = anio
        self.estado_restauracion = estado_restauracion
        self.stock = stock
        self.precio_unitario = precio_unitario
        self.formato = formato
        Pelicula.peliculas.append(self.titulo)

    def movie_available(self, titulo, stock):
        if titulo:
            print(f"La pelicula {self.titulo} esta '{self.stock}'")
            print(f"Titulo: {self.titulo}")
            print(f"Formato: {self.formato}")
            print(f"Stock: {self.stock}")
        else:
            print(f"Titulo no encontrado {self.titulo}")

    def mostrar():
        titulo = input("que pelicula busca?: ")
        movie_available(self, titulo, stock)