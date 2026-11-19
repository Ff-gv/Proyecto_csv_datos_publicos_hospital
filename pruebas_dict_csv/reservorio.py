import random

k = 10
reservorio = []
i = 0

for numero in range(1, 1001):  # Simula un archivo ordenado del 1 al 1000
    if i < k:
        reservorio.append(numero)
    else:
        j = random.randint(0, i)
        if j < k:
            reservorio[j] = numero
    i += 1
print(reservorio)