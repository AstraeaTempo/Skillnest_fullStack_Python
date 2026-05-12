#Plataforma de Steaming
class suscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estandar": 5.99, "Premium": 10.99}
#-------------------------------------------------------------------------
    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

#-------------------------------------------------------------------------
    def realizar_pago(self, monto):
        self.saldo_pendiente = self.saldo_pendiente - monto
        print("Usuario:", self.usuario)
        print("Monto pagado:", monto)
        print("Saldo actual:", self.saldo_pendiente)
#-------------------------------------------------------------------------
    def cambiar_suscripcion(self, nuevo_tipo):
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente = self.saldo_pendiente + self.costo_mensual
        print("Cambio de plan a:", nuevo_tipo)

#-------------------------------------------------------------------------
    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print("Acceso denegado")
        else:
            print("Acceso permitido para", self.usuario)

#-------------------------------------------------------------------------
    def mostrar_info_suscripcion(self):
        print("Nombre:", self.usuario)
        print("Suscripcion:", self.tipo_suscripcion)
        print("Costo:", self.costo_mensual)
        print("Saldo:", self.saldo_pendiente)

#________________________________________Fuera de funciones______________________________________________

print("--- MIYANO INFO ---")
u1 = suscripcionStreaming("Miyano", "Estandar")
u1.ver_contenido_exclusivo()
u1.cambiar_suscripcion("Estandar")
u1.realizar_pago(5.99)
u1.mostrar_info_suscripcion()

print("--- SASAKI INFO ---")
u2 = suscripcionStreaming("Sasaki", "Premium")
u2.ver_contenido_exclusivo()
u2.cambiar_suscripcion("Premium")
u2.realizar_pago(6.00)
u2.realizar_pago(10.00)
u2.mostrar_info_suscripcion()

print("--- HORI INFO ---")
u3 = suscripcionStreaming("Hori", "Gratis")
u3.realizar_pago(0)
u3.ver_contenido_exclusivo()
u3.mostrar_info_suscripcion()