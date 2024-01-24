"""Veamos un ejemplo. Creemos el archivo now.txt dentro del sistema.
El archivo almacena la fecha en la cual se ejecutó el script.
Para ello nuestro código puede quedar de la siguiente manera.
"""
import time
from datetime import datetime
fecha = str(datetime.now())

try:
    with open('now.txt', 'a') as file:
        for i in range(5):
            time.sleep(1)
            file.write(fecha + '\n')

except OSError:
    print('No fue posible crear el archivo')
    
