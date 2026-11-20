import random
"""
Toma desde una una lista o cualquier cosa iterable, luego agrega
entradas hasta que sea igual a la cantidad k, dentro del rango u ente 
iterable.

"""
#k es total de muestras a tomar
k = 10
#donde se guarda todo al final del ciclo for
reservorio = []
#contador
i = 0

for numero in range(1, 1001):  # Simula un archivo ordenado del 1 al 1000
    if i < k:
        #como se usa append, solo se agregan 10 numeros, las demas veces
        #vuelve a pasar y sobreescibir encima de esos 10 numeros
        reservorio.append(numero)
        print(reservorio)
        #aca secuencialmente entran numeros del 1 al 10
    else:
        j = random.randint(0, i)
        print(f"j es: {j}")
        #aca se generan numeros al azar en j
        if j < k:
            #cuando j esta dentro del limite de k, regenera los numeros
            #y los sobreescribe, como el rango es 1001, lo 
            #hace 1000 veces
            
            #una mejor explicacion, se genera un numero al azar entre
            #0 a i, j. Siempre y cuando j genere un numero menor a k
            #este numero entrara como reemplazo. pero con cada sucesion
            #es mas dificil reemplazar un numero una vez el rango aumenta
            #la razon es que el limite donde se genera el numero, que es
            #random.randint, va de 0 a i. Mientras mas alto, mas dificil es
            #que salga un numero que sea menor a k
            reservorio[j] = numero
            #una vez salga un numero generado al azar, se escribe la iteracion
            #numero del rango en el lugar al azar que salio reservorio j
            #es como jugar a la silla, si te toca una silla j, el numero
            #la toma
    i += 1
print(reservorio)