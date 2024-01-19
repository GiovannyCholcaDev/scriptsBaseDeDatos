"""Lectura bajo contexto
Otra forma de leer un archivo, y de hecho mucho más recomendable, es través de with. 
Veamos un ejemplo, recorramos todas las líneas del archivo ips.txt.
"""
try:
    with open('ips.txt') as file:
        for line in file.readlines():
            print(line)

except OSError:
    print('No fue posible leer el archivo')

""""
Cómo podemos observar, al nosotros trabajar con with, no será necesario cerrar el archivo de forma explícita.
Python lo hará una vez el bloque finalice, liberando así el recurso.
De forma personal recomiendo hacer uso de _with_siempre que trabajemos con archivos,
de esta forma obtendremos un código mucho más legible y fácil de mantener,
además por supuesto de optimizar recursos como lo es el uso de memoria
"""