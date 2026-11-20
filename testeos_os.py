#aca uso la clave directamente del diccionario para obtener
#el directorio de trabajo
import os

print(os.environ["PWD"])
#este es mas seguro, sigue donde mi programa viaja en
#directorios, por lo que hay que usar este
print(os.getcwd())
#pero tambien se puede usar getcwd para obtener el directorio]
#de trabajo
print(os.getlogin())
print(os.getpid())

print(sys.getfilesystemencoding()) 
print(os.getresuid())
#Retorna una tupla (ruid, euid, suid) que denota los ID de usuario reales, efectivos y guardados del proceso actual.
# esto significa que devuelve en mi caso (1000, 1000, 1000). Si el usuario es root devuelve (0, 0, 0)
#print(os.setregid(1001,1001))
#esto cambiaria los permisos de usuario, pero saldria PermissionError
#tendria que hacerse con sudo la ejecucion de este script
os.rename("1.txt","190.txt")
try:
    print(os.setregid(1001,1001))
except PermissionError as e:
    print(f"{e}: Usuario no es root.")
print(os.uname())
def sys_info_1():
    with open("sys_info_1.txt","w") as texto_sys:
        v,w,x,y,z= os.uname()
        texto_sys.write(f'{v} \n')
        texto_sys.write(f'{w} \n')
        texto_sys.write(f'{x} \n')
        texto_sys.write(f'{y} \n')
        texto_sys.write(f'{z} \n')

def sys_info_2():
    with open("sys_info_2.txt","w") as texto_sys:
        x = str(os.uname())
        texto_sys.write(x)
def mk_dir_funct():
    nombre_ingreso =input("ingrese nombre directorio: ")
    os.mkdir(nombre_ingreso)
    os.chdir(nombre_ingreso)
    sys_info_1()
    sys_info_2() 
    print(os.getcwd())
mk_dir_funct()


#aca sale todos los datos referentes al ambiente de mi os
# print(os.environ)
#esto obtiene un diccionario
#por lo que write no funcionaria
import os

def extraer_environ():
    """aca toma diccionario os.environ y escribe como iteracion
la clave y valor en un documento de texto"""
    print(os.environ["HOME"])
    with open("environ_os.txt","w") as txt_n:
        for a,b in os.environ.items():
            txt_n.write(f"{a}:{b}+\n")

def mk_dir_funct():
    try:
        nombre_ingreso =input("ingrese nombre directorio: ")
        os.mkdir(nombre_ingreso)
        os.chdir(nombre_ingreso)
    except FileExistsError:
        print("Directorio ya se encuentra creado.")    
    print(os.getcwd())