import mysql.connector

class Conexion:

    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Polyglot#3000",
            database="instituto",
            port = "3307"
        )