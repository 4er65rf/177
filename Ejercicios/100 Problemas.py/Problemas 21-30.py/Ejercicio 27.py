#27.Crear un conversor de unidades.

print ("Conversor de unidades")
print ("1. Convertir de metros a centímetros")
print ("2. Convertir de centímetros a metros")
print ("3. Convertir de kilómetros a metros")
print ("4. Convertir de metros a kilómetros")

op = input("Seleccione una opción: \n")

if op == '1':
    metros = float(input("Ingrese la cantidad de metros: "))
    centimetros = metros * 100
    print(f"{metros} metros son {centimetros} centímetros")
elif op == '2':
    centimetros = float(input("Ingrese la cantidad de centímetros: "))
    metros = centimetros / 100
    print(f"{centimetros} centímetros son {metros} metros")
elif op == '3':
    kilometros = float(input("Ingrese la cantidad de kilómetros: "))
    metros = kilometros * 1000
    print(f"{kilometros} kilómetros son {metros} metros")
elif op == '4':
    metros = float(input("Ingrese la cantidad de metros: "))
    kilometros = metros / 1000
    print(f"{metros} metros son {kilometros} kilómetros")
else:
    print("Opción no válida")
print("Fin del programa")


