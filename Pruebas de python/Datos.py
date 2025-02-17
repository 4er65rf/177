
Lista = ['Nombre', 'Lugar de Nacimiento', 'fecha de nacimiento']
Datos = {'Jhon', 'Eliysum, Eridano II', '07/marzo/2511'}
DatosAlumno= [Lista,Datos]
Mat={}
Mat['S-117']=DatosAlumno
print(Mat)

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad < 10:
    print(f"{nombre}, debes ir acompañado de un adulto.")
elif edad < 18:
    print(f"{nombre}, puedes entrar solo, pero algunas atracciones están restringidas.")
else:
    print(f"{nombre}, puedes entrar a todas las atracciones.")


edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")

edad = 25
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puedes manejar.")
else:
    print("No puedes manejar.")
    
     
