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

# ID del cliente que deseas borrar
id_cliente = 4  # ID del cliente que deseas borrar

# Ejecutar una consulta DELETE para borrar un cliente por ID
consulta_delete = """
    DELETE FROM cliente
    WHERE id = %s
"""

# Ejecutar la consulta DELETE con los parámetros
cursor.execute(consulta_delete, (id_cliente,))

# Confirmar la transacción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
