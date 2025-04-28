#29.Generar y analizar datos estadísticos.

with open("archivo.txt", "w") as archivo:
    archivo.write("4rfrqv3rg3554h.\n")
    archivo.write("24232errrff253g3.\n")
print ("Archivo creado con éxito")

with open("archivo.txt", "r") as archivo:
    data = archivo.readlines()
import statistics as stats

for i in data:
    print(i)
    print("Media:", stats.mean([int(j) for j in i if j.isdigit()]))
    print("Moda:", stats.mode([int(j) for j in i if j.isdigit()]))
    print("Desviación estándar:", stats.stdev([int(j) for j in i if j.isdigit()]))
    print("Varianza:", stats.variance([int(j) for j in i if j.isdigit()]))
    print("\n")