# Función para escribir en un archivo
def escribir_en_archivo(nombre_archivo, texto):
    with open(nombre_archivo, 'w') as archivo:  # 'w' para escribir (sobrescribir el archivo)
        archivo.write(texto)
    print(f"El texto ha sido escrito en {nombre_archivo}.")

# Función para leer el contenido de un archivo
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:  # 'r' para leer
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return f"El archivo {nombre_archivo} no existe."

# Función para modificar un archivo (agregar texto al final)
def modificar_archivo(nombre_archivo, texto_a_agregar):
    with open(nombre_archivo, 'a') as archivo:  # 'a' para agregar al final del archivo
        archivo.write(texto_a_agregar)
    print(f"El texto ha sido agregado a {nombre_archivo}.")

# Programa principal
def menu():
    nombre_archivo = input("Ingresa el nombre del archivo: ")

    while True:
        print("\nOpciones:")
        print("1. Escribir en el archivo")
        print("2. Leer el archivo")
        print("3. Modificar el archivo")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            texto = input("Ingresa el texto que deseas escribir en el archivo: ")
            escribir_en_archivo(nombre_archivo, texto)
        elif opcion == '2':
            contenido = leer_archivo(nombre_archivo)
            print(f"\nContenido del archivo {nombre_archivo}:\n{contenido}")
        elif opcion == '3':
            texto_a_agregar = input("Ingresa el texto que deseas agregar al archivo: ")
            modificar_archivo(nombre_archivo, texto_a_agregar)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor selecciona entre 1 y 4.")

# Ejecutar el menú
menu()