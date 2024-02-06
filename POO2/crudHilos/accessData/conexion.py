import mysql.connector



class MySQLConnection:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None


    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
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

