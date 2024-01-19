"""Veamos un ejemplo. Creemos el archivo now.txt dentro del sistema.
El archivo almacena la fecha en la cual se ejecutó el script.
Para ello nuestro código puede quedar de la siguiente manera.
"""

import time
from datetime import datetime

"""
import time
from datetime import datetime

if __name__ == '__main__':
    with open('dates.txt', 'a') as file:

        while True:
            time.sleep(1)
            file.write(str(datetime.now()) + '\n')
"""

"""En este caso utilizamos el modo a para crear el archivo en caso este no exista y añadir el nuevo contenido al final de este."""

print(__name__)
with open('dates.txt', 'a') as file:
    for i in range(3):
        time.sleep(1)
        file.write(str(datetime.now()) + '\n')