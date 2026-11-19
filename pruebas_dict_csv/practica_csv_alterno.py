import csv
import random
from sample_extract_institucion import extract_institucion
def muestra_csv_exploracion(doc):
    lista_unica = set() 
    headers = csv.Sniffer().has_header(doc)
    print(headers)
    scan_count = 1
    while scan_count <= 3:
        print(f"escaneo en progreso ... |{scan_count}| ")
        scan_count +=1
        with open(doc,mode="r",encoding="latin-1") as sample:
            sample_writing = csv.reader(sample,delimiter=';')
            header_csv = next(sample_writing)
            lista_lect = list(sample_writing)
            muestra = random.sample(lista_lect,3000)
        with open("sample1.csv",mode="w",newline='') as sample_csv:
            archivo_csv = csv.writer(sample_csv,delimiter=";")
            archivo_csv.writerow(header_csv)
            archivo_csv.writerows(muestra)
        extract_institucion("sample1.csv",lista_unica,scan_count)
        
        
muestra_csv_exploracion("07OCCompraAgil.csv")