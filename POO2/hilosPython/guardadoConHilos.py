import mysql.connector
from datetime import datetime
import threading

def coneccionSql():
    conexion = mysql.connector.connect(
        host="itsjapon.cc09no1kilik.us-east-2.rds.amazonaws.com",
        user="admin",
        password="baseDeDatos2japon",
        database="basepoo"
    )

# Función para insertar direcciones IP en la base de datos
def insertar_ips1():
    # Configurar la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="itsjapon.cc09no1kilik.us-east-2.rds.amazonaws.com",
        user="admin",
        password="baseDeDatos2japon",
        database="basepoo"
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta INSERT para insertar una nueva dirección IP
    consulta_insert = """
        INSERT INTO direccionesips (direccion, fecha)
        VALUES (%s, NOW())
    """

    # Manejador de archivos: Seleccionar archivo de una ruta
    file_path = 'ips1.txt'
    #print('Ini:', datetime.now())
    # Recorrer el archivo
    file = open(file_path)
    for line in file.readlines():
        cuenta = line.strip()
        cursor.execute(consulta_insert, (cuenta,))

    #print('Fin:', datetime.now())
    file.close()

    # Confirmar la transacción
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()


def insertar_ips2():
    # Configurar la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="itsjapon.cc09no1kilik.us-east-2.rds.amazonaws.com",
        user="admin",
        password="baseDeDatos2japon",
        database="basepoo"
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta INSERT para insertar una nueva dirección IP
    consulta_insert = """
        INSERT INTO direccionesips (direccion, fecha)
        VALUES (%s, NOW())
    """

    # Manejador de archivos: Seleccionar archivo de una ruta
    file_path = 'ips2.txt'
    #print('Ini:', datetime.now())
    # Recorrer el archivo
    file = open(file_path)
    for line in file.readlines():
        cuenta = line.strip()
        cursor.execute(consulta_insert, (cuenta,))

    #print('Fin:', datetime.now())
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
hilo_ips1 = threading.Thread(target=insertar_ips1)
hilo_ips2 = threading.Thread(target=insertar_ips2)

# Iniciar los hilos
hilo_ips1.start() 

hilo_ips2.start() 

#print("Finalizado.")
