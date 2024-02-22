from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estudiante(Base):

    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre =  Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)
    mail =  Column(String(50))
    matricula =  Column(String(50))
    carrera = Column(String(50))


