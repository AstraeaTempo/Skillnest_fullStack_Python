#Creación de la clase usuario - Entidad
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
catalina = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Miyagi
print(miyagi.email) #Imprime: miyagi@codingdojo.la
print(miyagi.limite_credito) #Imprime: 30000
print(miyagi.saldo_pagar) #Imprime: 0

daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

#Imprimir
print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido) #Imprime: Larusso
print(daniel.email) #Imprime: daniel@gmail.com
print(daniel.limite_credito) #Imprime: 100000
print(daniel.saldo_pagar) #Imprime: 300000

#Valores a nueva instancia
catalina.nombre = "Catalina"
catalina.apellido = "Acosta"
catalina.email = "catalina01acost@gmail.com"
catalina.limite_credito = 50000
catalina.saldo_pagar = 0

#Imprime
print(catalina.nombre)
print(catalina.apellido)
print(catalina.email)
print(catalina.limite_credito)
print(catalina.saldo_pagar)

#Imprime los 3 nombres
print(miyagi.nombre)
print(daniel.nombre)
print(catalina.nombre)