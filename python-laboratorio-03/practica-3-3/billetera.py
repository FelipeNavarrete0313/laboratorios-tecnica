class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False
        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0 or monto > self.saldo:
            return False
        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo

if __name__ == "__main__":
    b1 = Billetera("Alejandro")
    b2 = Billetera("Valentina")

    b1.registrar_ingreso(150000)
    b1.registrar_gasto(40000)

    b2.registrar_ingreso(50000)
    b2.registrar_gasto(80000)

    print(f"Saldo {b1.titular}: ${b1.consultar_saldo():,.0f}")
    print(f"Saldo {b2.titular}: ${b2.consultar_saldo():,.0f}")
