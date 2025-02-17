#26.Implementar una agenda de contactos.

bandera= True
contador = 1
ListaContactos = list()

print("Ingrese el identificador y el número de contacto")
while bandera:
    op = input(f"Cantidad de contactos: {contador-1} \n Desea agregar un contacto?(S/N): ")
    if op.lower() == 's':
        contacto = dict()
        contacto["identificador"] = input(f"Ingrese el identificador de contacto {contador}: ")
        contacto["número"] = input(f"Ingrese el número de contacto {contador}: ")
        contador += 1
        ListaContactos.append(contacto)
    else:
        print("Lista de contactos")
        for contacto in ListaContactos:
            print(contacto["identificador"], contacto["número"])
        bandera = False

print("Fin del programa")







