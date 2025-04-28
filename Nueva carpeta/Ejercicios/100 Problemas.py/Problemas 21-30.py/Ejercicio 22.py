#22.Simular el lanzamiento de un dado y una moneda

print ("Simular el lanzamiento de un dado y una moneda")

import random

print(" 1. Dado")
print(" 2. Moneda")

figura = int(input("Selecciona una figura:\n "))

if figura == 1:
    dado = random.randint(1, 6)
    print("El dado cayó en: ", dado)

elif figura == 2:
    moneda = random.randint(0, 1)
    if moneda == 0:
        print("La moneda cayó en: Cara")
    else:
        print("La moneda cayó en: Aguila")

print("Fin del programa")
