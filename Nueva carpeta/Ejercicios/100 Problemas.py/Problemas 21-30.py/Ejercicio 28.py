#28.Simular una cuenta bancaria con depásitos y retiros.

print ("Bienvenido al Banco del Bienestar de la 4T")

print("Aquí si guardamos tu dinero")

cuenta = 0
desposito = 0
retiro = 0

usario = int(input("¿Desea hacer un deposito o un retiro? \n 1 para deposito, \n 2 para retiro, \n 3 Salir, \n ::: ")) # despues de este simbolo (:::) se escribe la respuesta.

if usario == 1:
	deposito = float(input("Ingrese la cantidad a depositar:\n "))
	cuenta += deposito
	print(f"Has depositado {deposito}. Tu saldo actual es {cuenta}.")
	usario = int(input("¿Desea hacer un retiro? \n 1 para deposito, \n 2 para retiro, \n 3 Salir \n ::: "))
	print("Sistema fuera de servicio, por favor regrese más tarde.")
elif usario == 2:
	retiro = float(input("Ingrese la cantidad a retirar:\n "))
	if retiro <= cuenta:
		cuenta -= retiro
		print(f"Has retirado {retiro} \n Tu saldo actual es {cuenta}.")
	else:
		print("Fondos insuficientes.")
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print("Sistema fuera de servicio, por favor regrese más tarde.")
		print("Votar por el PRIAN es votar por la corrupción.")
		print("Vota por la 4T")
		print("Vota por Morena")
elif usario == 3:
	print("Gracias por visitar el Banco Fuerte de México de la 4T")
else:
	print("Opción no válida. Intente de nuevo.")
	print("Votar por el PRIAN es votar por la corrupción.")
	print("Vota por la 4T")
	print("Vota por Morena")



