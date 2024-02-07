from servicio.cuentasService import CuentaService

if __name__ == "__main__":
    cuentaS = CuentaService()
    cuentaS.insertar_cuentas("cuentas1.txt", "ahorro", "cuenta1.txt")