'''
CUENTA BANCARIA 
Crea una clase "CuentaBancaria" con atributos como número de cuenta y 
saldo. Implementa métodos para depositar y retirar dinero, y muestra el 
saldo actual.
'''
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo = 0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Se depositaron {monto} EU. Saldo actual: {self.saldo} EU")

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Se retiraron {monto} EU. Saldo actual: {self.saldo} EU")

        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo} EU")

# Ejemplo de uso
cuenta = CuentaBancaria("1200", 100) # numero de cuenta bancaria 1200 y tiene 100
cuenta.depositar(100)
cuenta.retirar(10)
cuenta.mostrar_saldo()