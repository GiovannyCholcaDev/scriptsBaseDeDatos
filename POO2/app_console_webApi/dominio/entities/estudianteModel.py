from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Estudiante(Base):

    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    edad = Column(Integer)
    mail = Column(String)
    matricula = Column(String)
    carrera = Column(String)


Base = declarative_base()