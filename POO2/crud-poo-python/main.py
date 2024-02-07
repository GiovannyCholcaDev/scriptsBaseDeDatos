from  conexion import ConexionDB


ConexionDB.cerrar_conexion

# Ejemplo de uso:
conexion = ConexionDB("tu_host", "tu_usuario", "tu_contraseña", "nombre_de_tu_base_de_datos")
cliente = Cliente(conexion)

# Crear un nuevo cliente
cliente.crear_cliente("Juan", "123456789")

# Leer todos los clientes
cliente.leer_clientes()

# Actualizar un cliente
cliente.actualizar_cliente(1, "Juan Pérez", "987654321")

# Borrar un cliente
cliente.borrar_cliente(1)

# Cerrar la conexión
conexion.cerrar_conexion()