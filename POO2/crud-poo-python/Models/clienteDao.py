class ClienteDao:
    
    def __init__(self, conexion):
        self.conexion = conexion

    def crear_cliente(self, nombre, telefono):
        consulta_insert = "INSERT INTO cliente (nombre, telefono) VALUES (%s, %s)"
        self.conexion.cursor.execute(consulta_insert, (nombre, telefono))
        self.conexion.conexion.commit()
        print("Cliente creado exitosamente.")

    def leer_clientes(self):
        consulta_select = "SELECT * FROM cliente"
        self.conexion.cursor.execute(consulta_select)
        clientes = self.conexion.cursor.fetchall()
        for cliente in clientes:
            print(cliente)

    def actualizar_cliente(self, id_cliente, nuevo_nombre, nuevo_telefono):
        consulta_update = "UPDATE cliente SET nombre = %s, telefono = %s WHERE id = %s"
        self.conexion.cursor.execute(consulta_update, (nuevo_nombre, nuevo_telefono, id_cliente))
        self.conexion.conexion.commit()
        print("Cliente actualizado exitosamente.")

    def borrar_cliente(self, id_cliente):
        consulta_delete = "DELETE FROM cliente WHERE id = %s"
        self.conexion.cursor.execute(consulta_delete, (id_cliente,))
        self.conexion.conexion.commit()
        print("Cliente eliminado exitosamente.")