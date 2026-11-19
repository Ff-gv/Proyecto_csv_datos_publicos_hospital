import csv
import random
import os

def muestra_csv_exploracion(doc):
    lista_unica = set()
    reserva = []
    limite = 3000
    count =  0
    scan_count = 1
    repetir= ""    
    verificacion = os.path.isfile("institucion.txt")
    """Funcion que explora un archivo CSV, realiza 3 escaneos de 3000 entradas
    al azar y por cada scan extrae los nombres de las instituciones """
    if verificacion == True:
        repetir = input("desea reescanear?: ").lower()
        if repetir == "si":
            rescan_institucion("institucion.txt")
        else:
            return print("operacion cancelada")
                
    while repetir == "si" or verificacion == False:
        while scan_count <= 3:
            print(f"escaneo en progreso ... |{scan_count}| ")
            scan_count +=1
            with open(doc,mode="r",encoding="latin-1") as sample:
                sample_writing = csv.reader(sample,delimiter=';')
                header_csv = next(sample_writing)
                for entrada in sample_writing:
                    if count < limite:
                        reserva.append(entrada)
                    else:
                        azar = random.randint(0, count)
                        if azar < limite:
                            reserva[azar] = entrada
                    count += 1        
            with open("sample1.csv",mode="w",newline='') as sample_csv:
                archivo_csv = csv.writer(sample_csv,delimiter=";")
                archivo_csv.writerow(header_csv)
                archivo_csv.writerows(reserva)
            extract_institucion("sample1.csv",lista_unica)
            if scan_count > 3:
                with open("institucion.txt",mode="w") as archivo:
                    for linea in lista_unica:
                        archivo.write(linea + "\n")
                        repetir = ""
            
                
                
            
    
    
    
def extract_institucion(doc,lista_1):
    lista_dic = []
    lista_unica = lista_1
    with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
        lectura = csv.DictReader(archivo,delimiter=";")
        for row in lectura:
            lista_dic.append({"institucion":row["Institucion"]})
            for institucion in lista_dic:
                lista_unica.add(institucion["institucion"])
        lista_dic = []
    return lista_unica

def rescan_institucion(doc):
    lista_unica = set()
    with open(doc,mode="r") as archivo:
        for line in archivo:
            lista_unica.add(line)
            return lista_unica
    return None
def extraer_año(doc):
    fecha = ""
    with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
        lectura = csv.DictReader(archivo,delimiter=";")
        for row in lectura:
            fecha ={"Fecha":row["FechaEnvioOC"]}

        lista_dic = []
    
            

muestra_csv_exploracion("07OCCompraAgil.csv")
#se podria guardar una lista en txt y llamarla para utilizarla como memoria
#de la lista unica
#pasar la escritura del archivo al final dee esta funcion en vez de estar en extract_institucion
#la escritura de la muestra puede ser opcional?