import mysql.connector
from datetime import datetime
import threading

# Función para insertar direcciones IP en la base de datos
def insertar_ips():
    # Configurar la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="itsjapon.cc09no1kilik.us-east-2.rds.amazonaws.com",
        user="admin",
        password="baseDeDatos2japon",
        database="pumablog"
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta INSERT para insertar una nueva dirección IP
    consulta_insert = """
        INSERT INTO direccionesips (direccion)
        VALUES (%s)
    """

    # Manejador de archivos: Seleccionar archivo de una ruta
    file_path = 'ipsc.txt'
    print('Ini:', datetime.now())
    # Recorrer el archivo
    file = open(file_path)
    for line in file.readlines():
        ip = line.strip()
        cursor.execute(consulta_insert, (ip,))

    print('Fin:', datetime.now())
    file.close()

    # Confirmar la transacción
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

# Función para imprimir la fecha y hora actual
def imprimir_fecha_hora():
    # Imprimir la fecha y hora actual
    fecha_y_hora_actual = datetime.now()
    print("Fecha y hora actual:", fecha_y_hora_actual)


# Crear los hilos para ejecutar las funciones
hilo_ips = threading.Thread(target=insertar_ips)


# Iniciar los hilos
hilo_ips.start()


print("Finalizado.")
