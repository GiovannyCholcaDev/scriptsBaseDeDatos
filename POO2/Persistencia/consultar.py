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

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM cliente")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()