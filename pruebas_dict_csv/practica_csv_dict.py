import csv
def muestra_csv(doc):
    sample_read_list= []
    with open(doc,mode="r",encoding="latin-1",newline="") as sample:
        sample_read = csv.DictReader(sample,delimiter=";")
        for row in sample_read:
            sample_read_list.append({"fecha_envio":row["FechaEnvioOC"],"codigo_envio":row["codigoOC"]})
            print(row['FechaEnvioOC'],row["codigoOC"])
    print(sample_read_list)
    with open("extract.txt",mode="w") as extractor:
        fieldnames=['fecha_envio','codigo_envio']
        write_txt = csv.DictWriter(extractor,fieldnames=fieldnames)
        write_txt.writerows(sample_read_list)

def muestra_csv_alt(doc):
    sample_read_list= []
    with open(doc,mode="r",encoding="latin-1",newline="") as sample:
        sample_read = csv.DictReader(sample,delimiter=";")
        for row in sample_read:
            sample_read_list.append({"fecha_envio":row["FechaEnvioOC"],"codigo_envio":row["codigoOC"]})
            print(row['FechaEnvioOC'],row["codigoOC"])
    print(sample_read_list)
    with open("extract_no_fecha.txt",mode="w") as extractor:
        fieldnames=['codigo_envio']
        write_txt = csv.DictWriter(extractor,fieldnames=fieldnames,extrasaction="ignore")
        write_txt.writerows(sample_read_list)
def muestra_csv_memoria(doc):
    sample_read_list= []
    memory_list = []
    with open(doc,mode="r",encoding="latin-1",newline="") as sample:
        sample_read = csv.DictReader(sample,delimiter=";")
        for row in sample_read:
            sample_read_list.append({"fecha_envio":row["FechaEnvioOC"],"codigo_envio":row["codigoOC"]})
            print(row['FechaEnvioOC'],row["codigoOC"])
        print(sample_read_list)
        for result in sample_read_list:
            for x,y in result.items():
                if x == "codigo_envio":
                    memory_list.append(y)
        print(memory_list)           
            
muestra_csv("papas.csv")
muestra_csv_alt("papas.csv")
muestra_csv_memoria("papas.csv")