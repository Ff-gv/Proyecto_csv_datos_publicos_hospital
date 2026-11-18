import csv
import os
import sys
from modulo_os import extraer_environ

#siempre usar utf-8 para que pueda trabajar adecuadamente
#esto obtiene el encoding print(sys.getfilesystemencoding()) 
def busqueda_fecha(doc):
    with open(doc,encoding="utf8",newline='') as csv_f:
    #probar con y sin newline=''
        doc_s = csv.reader(csv_f,delimiter=' ', quotechar="|")
        for row in doc_s:
            print(', '.join(row))

#aca uso la clave directamente del diccionario para obtener
#el directorio de trabajo
print(os.environ["PWD"])
#este es mas seguro, sigue donde mi programa viaja en
#directorios, por lo que hay que usar este
print(os.getcwd())
#pero tambien se puede usar getcwd para obtener el directorio]
#de trabajo

print(sys.getfilesystemencoding()) 
extraer_environ()