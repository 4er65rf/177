#24.Calcular la suma de una serie numérica.

print("Calcular la suma de una serie numérica")

print("1. Serie de números pares")

print("2. Serie de números impares")

opcion = int(input("Ingrese la opción: "))
n = int(input("Ingrese el número de términos: "))
suma = 0

if opcion == 1:
    for i in range(1, n + 1):
        suma += 2 * i
    print("La suma de la serie de números pares es:", suma)
    print("Fin del programa")
elif opcion == 2:
    for i in range(1, n + 1):
        suma += 2 * i - 1
    print("La suma de la serie de números impares es:", suma)
    print("Fin del programa")

