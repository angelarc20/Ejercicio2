from Cuenta import Cuenta
from Ingresos import Ingresos
from Egresos import Egresos

finanzas = Cuenta()
registroIngre = Ingresos()
registroEgre = Egresos()

while True:
    Menu = """Ingrese el número correspondiente a la opción que desee:
    0-Salir de la aplicación
    1-Registrar ingreso
    2-Registrar egreso
    3-Solicitar reporte de ingresos
    4-Solicitar reporte de egresos
    5-Solicitar reporte de transacciones (ingresos y egresos)
    6-Solicitar saldo en cuenta"""
    print(Menu)
    opcion = int(input("¿Cual es su opción deseada?"))
    if opcion == 0:
        break
    elif opcion == 1:
        cantIngreso = round(float(input("Digite la cantidad que desea ingresar a su cuenta")), 2)
        finanzas.registrarIngre(registroIngre.agregarIngreso(cantIngreso))
    elif opcion == 2:
        cantEgreso = round(float(input("Digite la cantidad a retirar")), 2)
        finanzas.registrarEgre(registroEgre.registrarEgre(cantEgreso))
    elif opcion == 3:
        ingresosTotales = registroIngre.ingresos
        print(f"Ha ingresado: {ingresosTotales}.")
    elif opcion == 4:
        egresosTotales = registroEgre.egresos
        print(f"Ha retirado: {egresosTotales}.")
    elif opcion == 5:
        reporteIngresos = registroIngre.ingresos
        reporteEgresos = registroEgre.egresos
        aviso = f"""Reporte de transacciones:
        Ingresos Totales: {reporteIngresos}.
        Egresos Totales: {reporteEgresos}. """
        print(aviso)
    elif opcion == 6:
        saldo = finanzas.cuenta
        print(f"Su saldo es de {saldo}.")
