import mysql.connector
from datetime import datetime

# Configurar la conexión a la base de datos
conexion = mysql.connector.connect(
    host="itsjapon.cc09no1kilik.us-east-2.rds.amazonaws.com",
    user="admin",
    password="baseDeDatos2japon",
    database="pumablog"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejecutar una consulta INSERT para insertar un nuevo cliente
consulta_insert = """
    INSERT INTO direccionesips (direccion)
    VALUES (%s)
"""

#manejador de archivos
#seleccionar archivo de una ruta
file_path = 'ipsc.txt'

#recorrer el archivo
print('Ini:', datetime.now())
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
