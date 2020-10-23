class Cuenta:
    def __init__(self):
        self.cuenta = 0.00

    def registrarIngre(self, nuevoIngre):
        self.cuenta += nuevoIngre
        print(f"Ingreso la cantidad de {nuevoIngre}.")
        print(f"Su cantidad actual es {self.cuenta}.")

    def registrarEgre(self, egreso):
        self.cuenta -= egreso
        print(f"Se retiro {egreso}.")
        print(f"Su cantidad es de {self.cuenta}.")
