"""Siempre que trabajemos con archivos una muy buena idea es utilizar un try y un except, 
esto para validar cualquier posible error de lectura o escritura. 
Por ejemplo, si intentamos obtener un archivo que no exista,
obtendremos el error : FileNotFoundError. 
 """
try:
    file_path = 'ipss.txt'
    #recorrer el archivo
    file = open(file_path)
    for line in file.readlines():
        print(line)
    
    file.close()
except FileNotFoundError as error:
    print(error)

#Podemos adecuar el script para una manejo más flexibles de los archivos.
try:
    file = open('ipss.txt')
except OSError:
    print('No fue posible leer el archivo')
else:
    file.close()


#Lectura de un Archivo
archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
archivo.close()

print(contenido)

