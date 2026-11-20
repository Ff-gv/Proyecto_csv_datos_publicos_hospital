from modulo_os import mk_dir_funct
from extraccion_hospital import extraer_observacion_hospital
from func_csv_exploracion import *
n = 1
nombre = ""
mk_dir_funct()
while n == 1:
    print(os.getcwd())
    print(       "|MENU PRINCIPAL"          )
    print("-"*20)
    print("1| Extraccion de muestras")
    print("2| Extraer observaciones de institucion")
    print("3| Salir")
    sel = input("ingrese una opcion: ")
    if sel == "1":
        print("|--Extraccion de muestra y archivo Institucion.txt--")
        print("|si es otro tipo seleccione opcion 2:")
        print(" |1  Compra agil")
        print(" |2  Ingresar archivo")
        sel = input()
        if sel == "1":
            muestra_csv_exploracion("07OCCompraAgil.csv")
        elif sel == "2":
            nombre = input("ingrese archivo a extraer: ")
            muestra_csv_exploracion(nombre)
    elif sel == "2":
        print(" Ingrese archivo a extraer")
        print("|si es otro tipo seleccione opcion 2:")
        print(" |1  Compra agil")
        print(" |2  Ingresar archivo")
        sel = input()
        if sel == "1":
            extraer_observacion_hospital("07OCCompraAgil.csv")
        elif sel == "2":
            nombre = input("ingrese archivo a extraer: ")
            extraer_observacion_hospital(nombre)
    elif sel == "3":
        n += 1
        
    #Se podria hacer una funcion que muestre una lsita de archivos
    #dentro de un directorio, para ver cuales son los que tienen
    #formato .csv y presentarlo al usuario