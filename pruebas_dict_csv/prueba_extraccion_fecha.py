import csv
import re
def extraer_año(doc):
    semestre_1 = "semestre_1"
    semestre_2 = "semestre_2"
    lista_fecha = set()
    lista_n = list()
    lista_trim = list()
    lista_1 = list()
    with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
        lectura = csv.DictReader(archivo,delimiter=";")
        for row in lectura:
            lista_fecha.add((row["FechaEnvioOC"].strip()))
        for x in lista_fecha:
            print(x)
            fecha = x[:10]
            lista_n.append(fecha)
        for x in lista_n:
            mes = x[3:5]
            if mes > "06":
                val = True
            elif mes < "06":
                val = False
                
        anio = lista_n[0][6:10]
        print(anio)
        print(val)
        
    #no creo que sea necesario colocarlo en la lsita, pero sirve para verificar
    #si la funcion es exitosa en filtrar
    #es mejor que si extraigo fechas para renombrar un archivo, lo haga
    #del sample1.csv        

    # print()
    # extraer_año = re.search(r"\d{2}-(\d{2})-(\d{4})",x)
    # año = extraer_año.group(2)
    # mes = extraer_año.group(1)
    # print(type(mes))
    # print(type(año))
    # print(mes)
    # print(año)
    # return año
extraer_año("07OCCompraAgil.csv")

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

# def extraer_año(doc):
#     fecha = ""
#     lista_fecha = ""
#     with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
#         lectura = csv.DictReader(archivo,delimiter=";")
#         fecha_ex = next(lectura)
#     print(type(fecha_ex))
#     x = fecha_ex["FechaEnvioOC"]
#     print(x)
#     extraer_año = re.search(r"\d{2}-(\d{2})-(\d{4})",x)
#     año = extraer_año.group(2)
#     mes = extraer_año.group(1)
#     print(type(mes))
#     print(type(año))
#     print(mes)
#     print(año)
#     return año
# extraer_año("07OCCompraAgil.csv")
    