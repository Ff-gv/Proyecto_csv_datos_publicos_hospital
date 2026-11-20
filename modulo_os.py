import os

def mk_dir_funct():
    try:
        nombre_ingreso = "Directorio_Compras"
        os.mkdir(nombre_ingreso)
    except FileExistsError:
        print("Directorio ya se encuentra creado.")    

