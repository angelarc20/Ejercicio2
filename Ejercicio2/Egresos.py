class Egresos:
    def __init__(self):
        self.egresos = 0.00

    def registrarEgre(self, cantEgreso):
        self.egresos += cantEgreso
        return cantEgreso
