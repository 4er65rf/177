#40. Crear una simulación de colas de espera.
print(f"Bienvenido IMSS de la 4T")
print(f"Desea hacer una cita?\n1. Si\n2. No")
opcion = int(input("Opcion: "))
if opcion == 1:
    print(f"Por favor espere su turno")
    import random
    import time
    si = 1
    no = 0
    
    #tiempo_espera_años = random.randint(1,120)
    #tiempo_espera_meses = random.randint(1, 12)
    #tiempo_espera_semanas= random.randint(1, 4)
    #tiempo_espera_dias = random.randint(1, 7)
    #tiempo_espera_horas = random.randint(1, 24)
    #tiempo_espera_minutos = random.randint(1, 60)
    tiempo_espera_segundos = random.randint(1, 60)
    #print(f"{tiempo_espera_años} años")
    #print(f"{tiempo_espera_meses} meses")
    #print(f"{tiempo_espera_semanas} semanas")
    #print(f"{tiempo_espera_dias} dias")
    #print(f"{tiempo_espera_horas} horas")
    #print(f"{tiempo_espera_minutos} minutos")
    print(f"Su tiempo de espera es de {tiempo_espera_segundos} segundos")
    
    #time.sleep(tiempo_espera_años)
    #time.sleep(tiempo_espera_meses)
    #time.sleep(tiempo_espera_semanas)
    #time.sleep(tiempo_espera_dias)
    #time.sleep(tiempo_espera_horas)
    #time.sleep(tiempo_espera_minutos)
    time.sleep(tiempo_espera_segundos)
    consultorio = random.randint(1, 10) 
    print(f"Su turno ha llegado, por favor pase al {consultorio} consultorio")
    print(f"Vaya a la farmacia por su medicamento, si es que hay")
    farmacia = random.randint(si, no)
    if farmacia == si:
        print(f"Su medicamento esta listo")
    else:
        print(f"No hay medicamento, vuelva a la semana siguiente")
    
elif opcion == 2:
    print(f"Gracias por su visita")