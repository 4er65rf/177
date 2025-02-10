 ##18. Resolver ecuaciones cuadráticas.

print("Resolución de ecuaciones cuadráticas")

import math

def ecuacionCuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        return "No tiene solución real"
    
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
print(ecuacionCuadratica(a, b, c))

print("Fin del programa")

