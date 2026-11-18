import csv
import os

#siempre usar utf-8 para que pueda trabajar adecuadamente
#esto obtiene el encoding print(sys.getfilesystemencoding()) 
def busqueda_fecha(doc):
    #con esto se si tiene encabezado, no es preciso pero es para verificar patrones
    headers = csv.Sniffer().has_header(doc)
    print(headers)
    lista_muestra = []
    with open(doc,mode="r",encoding="latin-1") as sample:
        sample_writing = csv.reader(sample,delimiter=';')
        for line in range(0,100):
            lista_muestra.append(next(sample_writing))
    with open("sample.csv",mode="w",newline='') as sample_csv:
        #csv.writer manda en delimitador, es el que controla si es , ; o cualquier otra puntuacion que delimita las columnas
        archivo_csv = csv.writer(sample_csv)
        archivo_csv.writerows(lista_muestra)
            
    with open(doc,encoding="latin-1",newline='',mode="r") as csv_f:
    #probar con y sin newline=''
        descubrir = csv.Sniffer().sniff(csv_f.read(100),delimiters=";")
        print(descubrir)
        
        
os.getcwd
busqueda_fecha("07OCCompraAgil.csv")