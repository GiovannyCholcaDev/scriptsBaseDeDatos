from dominio.entities.estudianteModel import Estudiante
from accessData.conexionORM import Database
from dominio.entities.modelsOrm import EstudianteBase

class EstudianteService:
    def __init__(self, database: Database):
        self.db = database

    def create_student(self, est: EstudianteBase):
        session = self.db.get_session()
        db_estudiante = Estudiante(nombre = est.nombre, apellido = est.apellido, edad = est.edad, mail = est.mail, matricula = est.matricula, carrera = est.carrera)
        session.add(db_estudiante)
        session.commit()
        session.refresh(db_estudiante)
        session.close()
        return db_estudiante

"""
    def get_person(self, person_id):
        session = self.db.get_session()
        person = session.query(Estudiante).filter(Estudiante.id == person_id).first()
        session.close()
        return person

    def update_person(self, person_id, nombre=None, apellido=None, edad=None, mail=None):
        session = self.db.get_session()
        person = session.query(Estudiante).filter(Estudiante.id == person_id).first()
        if nombre:
            person.nombre = nombre
        if apellido:
            person.apellido = apellido
        if edad:
            person.edad = edad
        if mail:
            person.mail = mail
        session.commit()
        session.refresh(person)
        session.close()
        return person

    def delete_person(self, person_id):
        session = self.db.get_session()
        person = session.query(Estudiante).filter(Estudiante.id == person_id).first()
        session.delete(person)
        session.commit()
        session.close()
        return {"message": "Deleted successfully"}
        
"""