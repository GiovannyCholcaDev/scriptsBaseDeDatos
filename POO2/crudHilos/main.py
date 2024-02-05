from accessData.conexion import MySQLConnection

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de MySQLConnection
    connection_manager = MySQLConnection(
        host="localhost",
        user="admin",
        password="basapon",
        database="baseo"
    )
    
    
    def insertar_cuentas():

        # Establecer la conexión
        connection_manager.connect()

        # Obtener la conexión
        connection = connection_manager.get_connection()

        # Aquí puedes usar 'connection' para realizar consultas, etc.
        cursor = connection_manager.cursor()

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
        
        file.close()

        # Confirmar la transacción
        connection_manager.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection_manager.close()
        # Cerrar la conexión cuando hayas terminado
