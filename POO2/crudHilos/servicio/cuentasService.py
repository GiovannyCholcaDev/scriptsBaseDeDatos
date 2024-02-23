from accessData.conexion import MySQLConnection

class CuentaService:

    def __init__(self):
        print('constructor CuentaService')
    
        self.consulta_insert = """
            INSERT INTO cuentas (numero_cuenta, tipo_cuenta, origen, fecha)
            VALUES (%s, %s, %s, NOW())
        """
    
    
    #def iniciarConexion(self):
        

    @classmethod
    def insertar_cuentas(self, file_path, tipo_cuenta, origen):
            
        print('iniciando metodo insertar_cuentas')


        self.connection_manager = MySQLConnection(
            host="localhost",
            user="admin",
            password="admin",
            database="pumasblog",
            port = "3306"
        )
        
        
        # Establecer la conexión
        self.connection_manager.connect()

        # Obtener la conexión
        connection = self.connection_manager.get_connection()

            # Aquí puedes usar 'connection' para realizar consultas, etc.
        cursor = connection.cursor()

            # Ejecutar una consulta INSERT para insertar una nueva dirección IP

            # Manejador de archivos: Seleccionar archivo de una ruta
            #file_path = 'cuentas1.txt'
            #print('Ini:', datetime.now())
            # Recorrer el archivo
        file = open(file_path)
        for line in file.readlines():
            cuenta = line.strip()
            #print(cuenta)
            cursor.execute(self.consulta_insert, (cuenta,tipo_cuenta, origen))
            
        file.close()

            # Confirmar la transacción
        connection.commit()

            # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
            # Cerrar la conexión cuando hayas terminado
            
        print('fin metodo')
