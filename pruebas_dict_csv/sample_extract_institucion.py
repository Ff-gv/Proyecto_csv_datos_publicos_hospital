import csv
def extract_institucion(doc,lista_1,scan_count):
    lista_dic_arch = []
    lista_unica = lista_1
    print(lista_1)
    with open(doc,mode="r",encoding="Latin-1",newline="") as archivo:
        lectura = csv.DictReader(archivo,delimiter=";")
        for row in lectura:
            lista_dic_arch.append({"institucion":row["Institucion"]})
            for institucion in lista_dic_arch:
                lista_unica.add(institucion["institucion"])
    #print(lista_unica)
    lista_dic_arch = []
    if scan_count == 3:
        try:
            with open("institucion.txt",mode="x") as archivo:
                for linea in lista_unica:
                    archivo.write(linea + "\n")
        except FileExistsError as e:
            print(f"archivo ya existe: {e}")
            with open("institucion.txt",mode="a") as archivo:
                for linea in lista_unica:
                    archivo.write(linea + "\n")
    return lista_unica
