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

# ID del cliente y nuevo nombre
id_cliente = 1  # ID del cliente que deseas actualizar
nuevo_nombre = "Giovanny"  # Nuevo nombre que deseas asignar

# Ejecutar una consulta UPDATE para actualizar el nombre por ID
consulta_update = """
    UPDATE cliente
    SET nombre = %s
    WHERE id = %s
"""

# Ejecutar la consulta UPDATE con los parámetros
cursor.execute(consulta_update, (nuevo_nombre, id_cliente))


# Confirmar la transacción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
