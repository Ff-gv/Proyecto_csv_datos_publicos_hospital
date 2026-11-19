import csv
import os

#siempre usar utf-8 para que pueda trabajar adecuadamente
#esto obtiene el encoding print(sys.getfilesystemencoding()) 
def muestra_csv(doc):
    #con esto se si tiene encabezado, no es preciso pero es para verificar patrones
    headers = csv.Sniffer().has_header(doc)
    print(headers)
    lista_muestra = []
    with open(doc,mode="r",encoding="latin-1") as sample:
        #csv reader lee el csv y convierte cada atributo de las entradas de una tabla en listas, se coloca el delimiter para
        #que pueda reconocer los espacios entre columnas
        sample_writing = csv.reader(sample,delimiter=';')
        for line in range(0,3000):
            lista_muestra.append(next(sample_writing))
    with open("sample.csv",mode="w",newline='') as sample_csv:
        #csv.writer manda en delimitador, es el que controla si es , ; o cualquier otra puntuacion que delimita las columnas
        archivo_csv = csv.writer(sample_csv)
        archivo_csv.writerows(lista_muestra)
def extraer_fecha():
    pass 
        
        
os.getcwd
muestra_csv("07OCCompraAgil.csv")