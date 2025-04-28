#21.Calcular el área y volumen de distintas figuras geométricas.

print ("Calcular el área y volumen")

print(" 1. Cuadrado(área)")
print(" 2. Cubo(volumen)")
print(" 3. Triángulo(área)")
print(" 4. Cono(volumen)")
print(" 5. Círculo(área)")
print(" 6. Esfera(volumen)")

figura = int(input("Selecciona una figura:\n "))

if figura == 1:
    lado = float(input("Ingresa el lado del cuadrado:\n "))
    area = lado**2
    print("El área del cuadrado es: ", area)
elif figura == 2:
    lado = float(input("Ingresa el lado del cubo:\n "))
    volumen = lado**3
    print("El volumen del cubo es: ", volumen)

elif figura == 3:
    base = float(input("Ingresa la base del triángulo:\n "))
    altura = float(input("Ingresa la altura del triángulo:\n "))
    area = (base * altura) / 2
    print("El área del triángulo es: ", area)

elif figura == 4:
    radio = float(input("Ingresa el radio del cono:\n "))
    altura = float(input("Ingresa la altura del cono:\n "))
    volumen = (3.1416 *(radio*2)* altura) / 3
    print("El volumen del cono es: ", volumen)

elif figura == 5:
    radio = float(input("Ingresa el radio del círculo:\n "))
    area = (3.1416 * (radio**2))
    print("El área del círculo es: ", area)

elif figura == 6:
    radio = float(input("Ingresa el radio de la esfera:\n "))
    volumen = ((4 * 3.1416 * (radio**3)) / 3)
    print("El volumen de la esfera es: ", volumen)

print("Fin del programa")


