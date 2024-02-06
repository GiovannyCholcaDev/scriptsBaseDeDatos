from accessData.conexion import MySQLConnection
import threading

# MAIN PRINCIPAL
if __name__ == "__main__":
    # Crear una instancia de MySQLConnection
    connection_manager = MySQLConnection(
        host="localhost",
        user="root",
        password="Polyglot#3000",
        database="pumasblog",
        port = "3307"
    )
    
    consulta_insert = """
            INSERT INTO cuentas (numero_cuenta, tipo_cuenta, origen, fecha)
                VALUES (%s, %s, %s, NOW())
        """
       
    def insertar_cuentas(file_path, tipo_cuenta, origen):
        
        print('iniciando metodo 1')

        # Establecer la conexión
        connection_manager.connect()

        # Obtener la conexión
        connection = connection_manager.get_connection()

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
            cursor.execute(consulta_insert, (cuenta,tipo_cuenta, origen))
        
        file.close()

        # Confirmar la transacción
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        # Cerrar la conexión cuando hayas terminado
        
        print('fin metodo 1')


      
    # Crear los hilos para ejecutar las funciones
    hilo_cuenta1 = threading.Thread(target=insertar_cuentas, args=("cuentas1.txt","ahorro", "cuenta1.txt" ))
    hilo_cuenta2 = threading.Thread(target=insertar_cuentas, args=("cuentas2.txt","corriente", "cuenta2.txt"))
    
    #hilo con tiempo de espera
    #hilo_cuenta2 = threading.Timer(5, function=insertar_cuentas2)


    # Iniciar los hilos
    hilo_cuenta1.start() 
    hilo_cuenta2.start()
    
    
    # esperamos a que terminen los hilos
    hilo_cuenta1.join()
    hilo_cuenta2.join()
    
    print('*******hilo programa principal************')