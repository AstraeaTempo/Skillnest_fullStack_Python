# Usuario-------------------------------------------------------------
class Usuario:
    usuarios = []
    
    def __init__(self, username, email, password, tipo_usuario):
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario
        self.saldo_pendiente = 0
        Usuario.usuarios.append(self.username)
        
    def realizar_pedido(self, pelicula, cantidad):
        pass
    
    def pagar_saldo(self, monto):
        pass
    
    def cambiar_contrasena(self, nueva_contrasena):
        pass
    
    def mostrar_usuarios(self):
        print("Imprimiendo información del usuario...")
        print(f"Nombre de usuario: {self.username}")
        print(f"Email: {self.username}")
        print(f"Tipo de usuario: {self.tipo_usuario}")
        print(f"Saldo pendiente: {self.saldo_pendiente}")

# Pedido -------------------------------------------------------------

class Pedido:
    pedidos = []

    def __init__(self, usuario, detalle_pedido, pelicula):
        self.usuario = usuario
        self.detalle_pedido = detalle_pedido
        self.pelicula = pelicula
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
        
    def actualizar_stock(self, cantidad):
        pass
    
    def restaurar_pelicula(self):
        pass
    
    def mostrar_info_pelicula(self):
        print("Mostrando información de la película...")
        print(f"Título: {self.titulo}")
        print(f"Año de publicación: {self.anio}")
        print(f"Formato: {self.formato}")
        print(f"Estado de restauración: {self.estado_restauracion}")
        print(f"Stock: {self.stock}")
        print(f"Precio unitario: {self.precio_unitario}")

    def j():
        pass