from dominio.persona import Persona
from accessData.conexion import Conexion

class PersonaService:

    def __init__(self):
        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()
        print("conexion iniciada")


    def crear_persona(self, persona):
        try:
            sql = "INSERT INTO persona (nombre, apellido, edad, mail) VALUES (%s, %s, %s, %s)"
            values = (persona.nombre, persona.apellido, persona.edad, persona.mail)
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("Persona creada exitosamente.")
        except Exception as err:
            print("Error en el insert:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def obtener_personas(self):
        try:
            personas = []
            self.cursor.execute("SELECT * FROM persona")
            for (id, nombre, apellido, edad, mail) in self.cursor:
                personas.append(Persona(id, nombre, apellido, edad, mail))
            return personas
        except Exception as err:
            print("Error en la ejecución de la consulta:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def actualizar_persona(self, persona):
        try:
            sql = "UPDATE persona SET nombre=%s, apellido=%s, edad=%s, mail=%s WHERE id=%s"
            values = (persona.nombre, persona.apellido, persona.edad, persona.mail, persona.id)
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("Persona actualizada exitosamente.")
        except Exception as err:
            print("Error en la actualizacion:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def eliminar_persona(self, id):
        try:
            sql = "DELETE FROM persona WHERE id=%s"
            self.cursor.execute(sql, (id,))
            self.connection.commit()
            print("Persona eliminada exitosamente.")
        except Exception as err:
            print("Error en la eliminación:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()


    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()