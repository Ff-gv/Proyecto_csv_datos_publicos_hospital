import csv
import re
def extraer_año(doc):
    fecha = ""
    lista_fecha = ""
    with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
        lectura = csv.DictReader(archivo,delimiter=";")
        fecha_ex = next(lectura)
    print(type(fecha_ex))
    x = fecha_ex["FechaEnvioOC"]
    print(x)
    extraer_año = re.search(r"\d{2}-\d{2}-(\d{4})",x)
    año = extraer_año.group(1)
    print(año)
extraer_año("sample1.csv")

# def extraer_año(doc):
#     fecha = ""
#     lista_fecha = ""
#     with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
#         lectura = csv.DictReader(archivo,delimiter=";")
#         for row in lectura[1]:
#             lista_fecha ={"Fecha":row["FechaEnvioOC"]}
#     print(type(lista_fecha))
#     x = lista_fecha["Fecha"]
#     print(x)
#     extraer_año = re.search(r"\d{2}-\d{2}-(\d{4})",x)
#     año = extraer_año.group(1)

    