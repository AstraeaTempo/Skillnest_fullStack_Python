#Métodos
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    #"-----------Monto-----------"
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    #-----------Aumento-----------"
    def aumentarCredito(self, aumento):
        self.limite_credito += aumento

    #-----------email-----------"
    def cambiarCorreo(self, email):
        self.email = email

#Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

#Comparas de Miyagi
print("-----------------Compras de Miyagi-----------------")
primeracompra = 2000
miyagi.hacer_compra(primeracompra)
print(f"Primera compra de {miyagi.nombre}: ${primeracompra}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: ${segundacompra}")
#Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")

#Compra de daniel 2 compras y muestra saldo a pagar ----
print("-----------------Compras de Daniel-----------------")
primeracompra = 45
daniel.hacer_compra(primeracompra)
print(f"Primera compra de {daniel.nombre}: ${primeracompra}")
segundacompra = 200
daniel.hacer_compra(segundacompra)
print(f"Segunda compra de {daniel.nombre}: ${segundacompra}")
#Imprimir cuanto credito le queda a Daniel
print(f"Credito disponible: ${daniel.limite_credito - daniel.saldo_pagar}")

print(miyagi.saldo_pagar) #Imprime: 2300
print(daniel.saldo_pagar) #Imprime: 245

#Tarea
'''
1.- Crear un nuevo método que permita aumentar el limite de crédito
Imprimir el nuevo limite de crédito

2.- Crearb un metodo que permita cambiar el correo de la instancia
Mostrar el nuevo Correo.
'''

print("-------Credito-------")
#Miyagi credito
miyagi.aumentarCredito(30000)
print(f"El nuevo limite de credito es: ${miyagi.limite_credito}")
#Daniel credito
daniel.aumentarCredito(10000)
print(f"El nuevo limite de credito es: ${daniel.limite_credito}")

print("-------Correo-------")
#Miyagi correo
miyagi.cambiarCorreo("miyagi347@gmail.com")
print(f"El nuevo gmail es: {miyagi.email}")
#Daniel correo
daniel.cambiarCorreo("daniel1234@gmail.com")
print(f"El nuevo gmail es: {daniel.email}")