from accessData.conexion import MySQLConnection

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de MySQLConnection
    connection_manager = MySQLConnection(
        host="itsoaaws.com",
        user="adin",
        password="basapon",
        database="baseo"
    )

    # Establecer la conexión
    connection_manager.connect()

    # Obtener la conexión
    connection = connection_manager.get_connection()

    # Aquí puedes usar 'connection' para realizar consultas, etc.

    # Cerrar la conexión cuando hayas terminado
    connection_manager.close()