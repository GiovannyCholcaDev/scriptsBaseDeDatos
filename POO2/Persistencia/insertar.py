# pip install mysql-connector-python

import mysql.connector


# Configurar la conexión a la base de datos
conexion = mysql.connector.connect(
    host="itsjapon.cc09no1kilik.us-east-2.rds.amazonaws.com",
    user="admin",
    password="baseDeDatos2japon",
    database="pumablog"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Datos del cliente a insertar
idcliente = "4"
nombreCliente = "Cesy"

# Ejecutar una consulta INSERT para insertar un nuevo cliente
consulta_insert = """
    INSERT INTO cliente (id, nombre)
    VALUES (%s, %s)
"""

# Ejecutar la consulta INSERT con los parámetros
cursor.execute(consulta_insert, (idcliente, nombreCliente))

# Confirmar la transacción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
