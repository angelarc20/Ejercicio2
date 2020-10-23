class Ingresos:
    def __init__(self):
        self.ingresos = 0.00

    def agregarIngreso(self, cantIngreso):
        self.ingresos += cantIngreso
        return cantIngreso
