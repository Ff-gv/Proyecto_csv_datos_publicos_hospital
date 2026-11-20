import csv
import os
def extraer_observacion_hospital(doc):
    lista_hospital = []
    with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
        lectura = csv.DictReader(archivo,delimiter=";")
        header = lectura.fieldnames
        for linea in lectura:
            x = linea["Institucion"]
            if x == "HOSPITAL CLINICO DE MAGALLANES DR. LAUTARO NAVARRO AVARIA":
                lista_hospital.append(linea)
    os.chdir("Directorio_Compras")
    with open("hospital_lautaro_navarro.csv",mode="w",encoding="Latin-1",newline="") as archivo:
        escritura = csv.DictWriter(archivo,delimiter=";",fieldnames=header)
        escritura.writeheader()
        escritura.writerows(lista_hospital)
    os.chdir("..")
# extraer_observacion_hospital("07OCCompraAgil.csv")
