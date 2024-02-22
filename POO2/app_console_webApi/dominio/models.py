class Persona:
    def __init__(self, id, nombre, apellido, edad, mail):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
        #print('clase persona')


class Estudiante(Persona):
    def __init__(self, id, nombre, apellido, edad, mail, matricula, carrera):
        super().__init__(id, nombre, apellido, edad, mail)
        self.matricula = matricula
        self.carrera = carrera
        #print('clase ESTUDIANTE')


