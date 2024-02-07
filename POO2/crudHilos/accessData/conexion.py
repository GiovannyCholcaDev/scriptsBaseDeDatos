import mysql.connector

class MySQLConnection:

    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            database="crud_persona"
            host="localhost",
            user="root",
            password="Polyglot#3000",
            database="pumasblog",
    )

    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        print('constructor MySQLConnection')

    @classmethod
    def connect(self, conexion):
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

    @classmethod
    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    @classmethod
    def get_connection(self):
        return self.connection
