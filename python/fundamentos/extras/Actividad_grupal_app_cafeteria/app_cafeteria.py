class CafeteriaCliente:

    total_clientes = []

    def __init__(self, nombre, puntos=0, saldo=0, membresia="Bronce"):
        self.nombre = nombre
        self.puntos_acumulados = puntos
        self.saldo_pendiente = saldo
        self.tipo_membresía = membresia

        CafeteriaCliente.total_clientes.append(self)

    def realizar_compra(self, monto):
        self.saldo_pendiente += monto
        self.puntos_acumulados += int(monto // 10)
        print(f"{self.nombre} realizó una compra. de {monto}")
        
    
    def pagar_saldo(self, monto):
        if monto <= 0:
            print("El monto a pagar debe ser mayor que 0.")
        elif monto >= self.saldo_pendiente:
            print(f"{self.nombre} ha pagado su saldo pendiente.")
            self.saldo_pendiente = 0
        else:
            self.saldo_pendiente -= monto
            print(
            f"{self.nombre} ha pagado {monto} de su saldo pendiente. "
            f"Saldo restante: {self.saldo_pendiente}"
        )

    @classmethod
    def mostrar_total_clientes(cls):
        return len(cls.total_clientes)
    
    @staticmethod
    def validar_membresia(tipo):
        if tipo:
            return True
        else:
            return False

c1 = CafeteriaCliente; ("Jose", 0, 0, "Bronce")
c2 = CafeteriaCliente; ("Felipe", 10, 10, "Plata")
c3 = CafeteriaCliente; ("Sofia", 10, 50, "Oro")