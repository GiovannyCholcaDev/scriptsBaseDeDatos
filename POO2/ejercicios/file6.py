#Manejo de Errores
""" 
Es importante tener en cuenta que al trabajar con archivos, pueden ocurrir errores, 
como archivos no encontrados o problemas de lectura/escritura.
Para manejar estos errores de manera efectiva, es recomendable utilizar bloques try y except.
"""


try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)
except FileNotFoundError:
    print("El archivo no se pudo encontrar.")
except Exception as e:
    print("Ocurrió un error:", e)



"""En este ejemplo, se intenta abrir un archivo que no existe, lo que generará una excepción FileNotFoundError. 
Utilizando bloques try y except, puedes manejar diferentes tipos de errores de manera adecuada. """