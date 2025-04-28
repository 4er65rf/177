#Ejercicio 8: Implementaci´on de Mergesort
#Ejemplo de entrada/salida:
#Entrada: [38, 27, 43, 3, 9, 82, 10]
#Salida: [3, 9, 10, 27, 38, 43, 82]

def merge_sort(arr):
    if len(arr) > 1: #len(numeros) #len() devuelve la longitud de la lista numeros
        mid = len(arr) // 2  # Encuentra el punto medio de la lista
        L = arr[:mid]  # Divide la lista en dos mitades
        R = arr[mid:]
        merge_sort(L)  # Ordena la primera mitad
        merge_sort(R)  # Ordena la segunda mitad
        i = j = k = 0
        # Copia los datos a las listas temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Verifica si quedan elementos en L[]
        while i < len(L): #while i < len(L): #mientras i sea menor que la longitud de L
            arr[k] = L[i] #arr[k] = L[i] #asigna el valor de L[i] a arr[k]
            i += 1
            k += 1
        # Verifica si quedan elementos en R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Solicita al usuario que ingrese una lista de números separados por comas
entrada = input("Ingrese una lista de números separados por comas: ")
try:#try se utiliza para manejar excepciones, es decir, errores que pueden ocurrir durante la ejecución del programa. En este caso, se utiliza para manejar el error que puede ocurrir si el usuario ingresa un valor no numérico en la lista de números.
    numeros = list(map(int, entrada.split(",")))  # Convierte la entrada en una lista de enteros
    print("Lista antes de ordenar:", numeros)  # Muestra la lista original
except ValueError:#except ValueError si el usuario ingresa un valor no numérico, se lanza una excepción ValueError y se imprime un mensaje de error.
    numeros = []
merge_sort(numeros)  # Llama a la función merge_sort para ordenar la lista
print("Lista después de ordenar:", numeros)  # Muestra la lista ordenada



