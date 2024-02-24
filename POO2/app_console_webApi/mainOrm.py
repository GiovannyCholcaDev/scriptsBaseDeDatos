from accessData.conexionORM import Database,DATABASE_URL
from dominio.entities.estudianteModel import Base, Estudiante 
from dominio.entities.modelsOrm import EstudianteBase
from servicio.estudianteORMService import EstudianteService
from servicio.genericService import GenericRepository


def mostrar_estudiante(estudiantes):
    for est in estudiantes:
        print(vars(est))


def main():

    estudiante_service = EstudianteService(db)

    studen_repository = GenericRepository[Estudiante](Estudiante, db)

    while True:
        print("\n--- MENU ---")
        print("1. Crear estudiante")
        print("2. Mostrar todos estudiantes")
        print("3. Mostrar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            mail = input("Ingrese el correo electrónico: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")

            student = EstudianteBase(None, nombre, apellido, edad, mail, matricula, carrera)
            """estudiante_service.create_student(student)"""
            student = studen_repository.create(nombre=student.nombre, apellido=student.apellido, edad=student.edad, mail=student.mail, matricula = student.matricula, carrera = student.carrera)

            print(vars(student))


        elif opcion == "2":
            #estudiante = estudiante_service.get_student_all()
            estudiante = studen_repository.getAll();
            mostrar_estudiante(estudiante)

        elif opcion == "3":
            estudianteId = int(input("Ingrese el ID del estudiante a consultar: "))
            #estudiante = estudiante_service.get_student(estudianteId)
            student = studen_repository.get(estudianteId)
            print(vars(student))


        elif opcion == "4":
            id_persona = int(input("Ingrese el ID de la persona que desea actualizar: "))
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            edad = int(input("Ingrese la nueva edad: "))
            mail = input("Ingrese el nuevo correo electrónico: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")
            student = EstudianteBase(id_persona, nombre, apellido, edad, mail, matricula, carrera)
            #estudiante_service.update_student(student)
            studen_repository.update(id_persona, student)
            print("Estudiante actualizado")
        elif opcion == "5":
            estudianteId = int(input("Ingrese el ID de la persona que desea eliminar: "))
            #estudiante_service.delete_person(estudianteId)
            studen_repository.delete(estudianteId)

        elif opcion == "6":
            estudiante_service.cerrarConexion()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    db = Database(DATABASE_URL)
    engine = db.engine
    # Crea todas las tablas definidas en el modelo
    #db.Base.metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    main()