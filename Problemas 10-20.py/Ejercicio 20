 ##20. Implementar búsqueda binaria y lineal.

print("Búsqueda binaria y lineal")

import random as rd

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

lista = [rd.randint(1, 100) for i in range(10)]
lista.sort()
print("Lista generada: ", lista)
elemento = rd.randint(1, 100)
print("Elemento a buscar: ", elemento)
print("Resultado de la búsqueda lineal: ", busqueda_lineal(lista, elemento))
print("Resultado de la búsqueda binaria: ", busqueda_binaria(lista, elemento))

print("Fin del programa")