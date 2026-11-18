#aca sale todos los datos referentes al ambiente de mi os
# print(os.environ)
#esto obtiene un diccionario
#por lo que write no funcionaria
import os

def extraer_environ():
    """aca toma diccionario os.environ y escribe como iteracion
la clave y valor en un documento de texto"""
    print(os.environ["HOME"])
    with open("environ_os.txt","w") as txt_n:
        for a,b in os.environ.items():
            txt_n.write(f"{a}:{b}+\n")

