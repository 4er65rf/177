 ##16. Contar el número de vocales y consonantes en una cadena.

print("Contar el número de voales y consonantes en una cadena")

print("Ingrese una cadena")
cadena = input()
vocales = 0
consonantes = 0
for i in cadena:
    if i in "aeiouAEIOU":
        vocales += 1
    elif i in "bcdfghjkLmnñpqrstvwxyzBCDFGHJKLMNÑPOQRSTVWXYZ":
        consonantes += 1
        print("El número de vocales es", vocales)
        print("El número de consonantes es", consonantes)

        print("Fin del programa")
        