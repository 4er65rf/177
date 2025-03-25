#40. Crear una simulación de colas de espera.

print(f"Desea hacer un tramite?\n1. Si\n2. No")
opcion = int(input("Opcion: "))
if opcion == 1:
    print(f"Bienvenido a la oficina de tramites\nPor favor espere su turno")
    import random
    import time

    # Simulando el tiempo de espera en segundos
    tiempo_espera = random.randint(1, 10)
    print(f"Su tiempo de espera es de {tiempo_espera} segundos")
    time.sleep(tiempo_espera)

    print(f"Su turno ha llegado, por favor pase a la ventanilla")

else:
    opcion = 2
    print(f"Gracias por su visita, vuelva pronto")