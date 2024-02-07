from dominio.persona import Persona
from servicio.personaService import PersonaService


def mostrar_personas(personas):
    for persona in personas:
        print(vars(persona))


def main():
    persona_service = PersonaService()

    while True:
        print("\n--- MENU ---")
        print("1. Crear persona")
        print("2. Mostrar personas")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            mail = input("Ingrese el correo electrónico: ")
            nueva_persona = Persona(None, nombre, apellido, edad, mail)
            persona_service.crear_persona(nueva_persona)

        elif opcion == "2":
            personas = persona_service.obtener_personas()
            mostrar_personas(personas)

        elif opcion == "3":
            id_persona = int(input("Ingrese el ID de la persona que desea actualizar: "))
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            edad = int(input("Ingrese la nueva edad: "))
            mail = input("Ingrese el nuevo correo electrónico: ")
            persona_actualizada = Persona(id_persona, nombre, apellido, edad, mail)
            persona_service.actualizar_persona(persona_actualizada)

        elif opcion == "4":
            id_persona = int(input("Ingrese el ID de la persona que desea eliminar: "))
            persona_service.eliminar_persona(id_persona)

        elif opcion == "5":
            persona_service.cerrar_conexion()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")



if __name__ == "__main__":
    main()