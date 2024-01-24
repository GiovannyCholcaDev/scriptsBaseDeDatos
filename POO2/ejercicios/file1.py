"""archivo = open("archivo.txt", "a")
contenido = archivo.read()
archivo.close()
print(contenido)"""
"""
from datetime import datetime
fecha = str(datetime.now())

archivo = open("nuevo_archivo.txt", "a")
archivo.write(fecha + '\n')
archivo.close()"""

from datetime import datetime
fecha = str(datetime.now())
try:
    with open('now.txt', 'w') as file:
        file.write(fecha + '\n')

except OSError:
    print('No fue posible crear el archivo')
    
