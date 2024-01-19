"""Veamos un ejemplo. Creemos el archivo now.txt dentro del sistema.
El archivo almacena la fecha en la cual se ejecutó el script.
Para ello nuestro código puede quedar de la siguiente manera.
"""

from datetime import datetime

fecha = str(datetime.now())
#w  a
try:
    with open('now.txt', 'w') as file:
        file.write(fecha + '\n')

except OSError:
    print('No fue posible crear el archivo')
    
