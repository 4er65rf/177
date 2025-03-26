#40. Crear una simulación de colas de espera.

print(f"Desea hacer un tramite?\n1. Si\n2. No")
opcion = int(input("Opcion: "))
if opcion == 1:
    print(f"Bienvenido a la oficina de tramites del IMSS\nPor favor espere su turno")
    import random
    import time

    tiempo_espera_años = random.randint(1,120)
    tiempo_espera_meses = random.randint(1, 12)
    tiempo_espera_semanas= random.randint(1, 4)
    tiempo_espera_dias = random.randint(1, 7)
    tiempo_espera_horas = random.randint(1, 24)
    tiempo_espera_minutos = random.randint(1, 60)
    tiempo_espera_segundos = random.randint(1, 60)
    print(f"Su tiempo de espera es de {tiempo_espera_años} años {tiempo_espera_meses} meses {tiempo_espera_semanas} semanas {tiempo_espera_dias} dias {tiempo_espera_horas} horas {tiempo_espera_minutos} minutos {tiempo_espera_segundos} segundos")
    time.sleep(tiempo_espera_años)
    time.sleep(tiempo_espera_meses)
    time.sleep(tiempo_espera_semanas)
    time.sleep(tiempo_espera_dias)
    time.sleep(tiempo_espera_horas)
    time.sleep(tiempo_espera_minutos)
    time.sleep(tiempo_espera_segundos)

    print(f"Su turno ha llegado, por favor pase a la ventanilla")

else:
    opcion = 2
    print(f"Gracias por su visita, vuelva pronto")