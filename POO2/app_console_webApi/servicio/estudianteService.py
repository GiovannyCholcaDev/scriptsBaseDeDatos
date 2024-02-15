from dominio.dominio import Estudiante
from accessData.conexion import Conexion

class EstudianteService:

    def __init__(self):
        pass


    def crear_estudiante(self, estudiante):
        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO estudiante (nombre, apellido, edad, mail, matricula, carrera) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (estudiante.nombre, estudiante.apellido, estudiante.edad, estudiante.mail, estudiante.matricula, estudiante.carrera)
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("Persona creada exitosamente.")
        except Exception as err:
            print("Error en el insert:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def obtener_estudiantes(self):
        try:
            self.connection = Conexion.obtener_conexion()
            self.cursor = self.connection.cursor()
            estudiantesList = []
            self.cursor.execute("SELECT * FROM estudiante")
            for (id, nombre, apellido, edad, mail, matricula, carrera) in self.cursor:
                estudiantesList.append(Estudiante(id, nombre, apellido, edad, mail, matricula, carrera))
            return estudiantesList
        except Exception as err:
            print("Error en la ejecución de la consulta:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def actualizar_estudiante(self, estudiante):
        try:
            self.connection = Conexion.obtener_conexion()
            self.cursor = self.connection.cursor()
            sql = "UPDATE estudiante SET nombre=%s, apellido=%s, edad=%s, mail=%s, matricula=%s, carrera=%s WHERE id=%s"
            values = (estudiante.nombre, estudiante.apellido, estudiante.edad, estudiante.mail, estudiante.matricula, estudiante.carrera, estudiante.id)
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("Estudiante actualizada exitosamente.")
        except Exception as err:
            print("Error en la actualizacion:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def eliminar_estudiante(self, id):
        try:
            self.connection = Conexion.obtener_conexion()
            self.cursor = self.connection.cursor()
            sql = "DELETE FROM estudiante WHERE id=%s"
            self.cursor.execute(sql, (id,))
            self.connection.commit()
            print("Estudiante eliminada exitosamente.")
        except Exception as err:
            print("Error en la eliminación:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()