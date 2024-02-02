import mysql.connector

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None


    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión establecida con éxito.")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    
    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

   
    def get_connection(self):
        return self.connection


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
