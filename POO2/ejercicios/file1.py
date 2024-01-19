# Abrir un Archivo para Lectura


archivo = open("ips.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)

"""
    archivo = open("mi_archivo.txt", "r"): Esta línea abre un archivo llamado "mi_archivo.txt" en modo de lectura ("r"). La función open() toma dos argumentos: el nombre del archivo y el modo de apertura. En este caso, el modo de apertura "r" indica que el archivo se abrirá en modo lectura.
    contenido = archivo.read(): Después de abrir el archivo, la función read() se utiliza para leer el contenido completo del archivo y asignarlo a la variable contenido. Esto carga todo el contenido del archivo en la memoria como una cadena.
    archivo.close(): Finalmente, se cierra el archivo utilizando el método close() para liberar los recursos y permitir que otros programas o partes del código accedan al archivo. Cerrar el archivo es una buena práctica para asegurarse de que los recursos se gestionen correctamente y el archivo se libere.
"""





#Abrir un Archivo para Escritura
# w  a
archivo = open("nuevo_archivo.txt", "w")
archivo.write("¡Hola, esto es un nuevo archivo!\n")
archivo.close()

"""
    archivo = open("nuevo_archivo.txt", "w"): Esta línea crea un objeto de archivo llamado archivo utilizando la función open(). El primer argumento "nuevo_archivo.txt" es el nombre del archivo que se abrirá o creará si no existe. El segundo argumento "w" especifica el modo de apertura, que en este caso es "escritura" (write). Si el archivo ya existe, este modo borrará su contenido existente y permitirá escribir nuevos datos en él. Si el archivo no existe, se creará.
    archivo.write("¡Hola, esto es un nuevo archivo!\n"): Esta línea utiliza el método write() para escribir la cadena "¡Hola, esto es un nuevo archivo!\n" en el archivo. El \n representa un carácter de nueva línea, lo que hace que la siguiente escritura comience en una nueva línea en el archivo.
    archivo.close(): Finalmente, esta línea cierra el archivo después de que hayas terminado de escribir en él. Es importante cerrar el archivo después de usarlo para liberar los recursos del sistema operativo asociados con él.

"""


#Abrir un Archivo para Agregar Contenido
archivo = open("mi_archivo.txt", "a")
archivo.write("Añadiendo más contenido al archivo.\n")
archivo.close()
"""
    archivo = open("mi_archivo.txt", "a"): Aquí se abre un archivo llamado "mi_archivo.txt" en modo de adición ("a"). El modo de adición ("a") indica que se abrirá el archivo en modo de escritura, pero si el archivo ya existe, el nuevo contenido se agregará al final del archivo sin sobrescribir el contenido existente. Si el archivo no existe, se creará uno nuevo.
    archivo.write("Añadiendo más contenido al archivo.\n"): Después de abrir el archivo en modo de adición, utilizamos el método write() para agregar la cadena "Añadiendo más contenido al archivo." al archivo. La cadena \n representa un salto de línea, lo que significa que el próximo contenido agregado estará en una nueva línea.
    archivo.close(): Finalmente, usamos el método close() para cerrar el archivo después de haber terminado de escribir en él. Cerrar el archivo es importante para asegurarse de que todos los cambios se guarden correctamente y para liberar los recursos asociados al archivo.
"""


#Lectura de un Archivo
archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
archivo.close()

print(contenido)



#Leer Líneas
archivo = open("mi_archivo.txt", "r")

linea1 = archivo.readline()
linea2 = archivo.readline()

archivo.close()

print(linea1)
print(linea2)