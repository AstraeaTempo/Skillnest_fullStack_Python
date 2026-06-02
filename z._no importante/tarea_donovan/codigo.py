# Usuario-------------------------------------------------------------
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

# Pedido -------------------------------------------------------------

class Pedido:
    pedidos = []

    def __init__(self, usuario):
        self.usuario = usuario
        Pedido.pedidos.append(self.usuario)

        def pedidos_realizados():
            pass #por mientras

# Pelicula -----------------------------------------------------------

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

    def movie_available(self, book_title, stock):
        if book_title:
            print(f"La pelicula {self.titulo} esta '{self.stock}'")
            print(f"Titulo: {self.titulo}")
            print(f"Formato: {self.formato}")
            return True
        else:
            print(f"Titulo no encontrado {self.titulo}")
            print(f"Stock: {self.stock}")
            return False
        
    