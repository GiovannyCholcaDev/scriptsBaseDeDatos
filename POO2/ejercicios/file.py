#manejador de archivos
#seleccionar archivo de una ruta
file_path = 'ips.txt'

#La función open retorna un objeto de tipo TextIOWrapper.
file = open(file_path)

type(file)
print(type(file))

content = file.read() 

# Cantidad de caracteres en el archivo
total = len(content)
print(total)

#terminado de utilizar un archivo debemos cerrarlo
#esto con la finalidad de liberar espacio en memoria y permitir que otros procesos puedan hacer uso de él.
file.close()

#recorrer el archivo
"""
file = open(file_path)
for line in file.readlines():
    print(line)
file.close()"""