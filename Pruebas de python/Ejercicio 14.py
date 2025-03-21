##14. Implementar distintos métodos de ordenamiento.
"""""""""""""""
print("Implementar distintos métodos de ordenamiento")
print("1. Bob")
print("2. Steve")
print("3. Isaac")
print("4. Jordan")
print("5. Louis")
opcion = int(input("Selecciona una opción:\n"))
if opcion == 1:
    def Bob (Lista):
        n = len(Lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if Lista[j] > Lista[j+1]:
                    Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
        return Lista

    Lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", Lista)
    print("Lista ordenada:", Bob (Lista))

elif opcion == 2:
    def Steve (Lista):
        n = len(Lista)
        for i in range(n):
            minimo = i
            for j in range(i+1, n):
                if Lista[j] < Lista[minimo]:
                    minimo = j
            Lista[i], Lista[minimo] = Lista[minimo], Lista[i]
        return Lista

    Lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", Lista)
    print("Lista ordenada:", Steve(Lista))

elif opcion == 3:
    def Isaac (Lista):
        n = len(Lista)
        for i in range(1, n):
            actual = Lista[i]
            j = i-1
            while j >= 0 and actual < Lista[j]:
                Lista[j+1] = Lista[j]
                j -= 1
            Lista[j+1] = actual
        return Lista

    Lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", Lista)
    print("Lista ordenada:", Isaac (Lista))

elif opcion == 4:
    def Jordan (Lista):
        if len(Lista) <= 1:
            return Lista
        else:
            pivote = Lista[0]
            menores=[x for x in Lista[Lista.index(pivote)+1:]if x<=pivote]
            mayores = [x for x in Lista[Lista.index(pivote)+1:] if x > pivote]
            return Jordan(menores)+[pivote]+Jordan(mayores)
        
        Lista =[64,34,25,12,22,11,90]
        print("Lista original:", Lista)
        print("Lista ordenada:", Jordan(Lista))

elif opcion == 5:
    def Louis(Lista):
        if len(Lista) > 1:
            mitad = len(Lista)//2
            L = Lista[:mitad]
            R = Lista[mitad:]
            Louis(L)
            Louis(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    Lista[k] = L[i]
                    i += 1
                else:
                    Lista[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                Lista[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                Lista[k] = R[j]
                j += 1
                k += 1
        return Lista

    Lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", Lista)
    Louis(Lista)
    print("Lista ordenada:", Lista)
else:
    print("Opción no válida")
    print("Fin del programa")

"""""""""""""""