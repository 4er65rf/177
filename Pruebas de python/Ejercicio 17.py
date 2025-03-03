## 17. Implementar estructuras de datos básicas: pila, cola y lista enlazada.

"""
print("Implementar estructuras de datos básicas: pila, cola y lista enlazada")

print("1. Pila")
print("2. Cola")
print("3. Lista enlazada")

opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    class Pila:
        def __init__(self):
            self.items = []

        def estaVacia(self):
            return self.items == []

        def incluir(self, item):
            self.items.append(item)

        def extraer(self):
            return self.items.pop()

        def inspeccionar(self):
            return self.items[len(self.items)-1]

        def tamano(self):
            return len(self.items)

    pila = Pila()
    print(pila.estaVacia())
    pila.incluir(4)
    pila.incluir('perro')
    print(pila.inspeccionar())
    pila.incluir(True)
    print(pila.tamano())
    print(pila.estaVacia())
    pila.incluir(8.4)
    print(pila.extraer())
    print(pila.extraer())
    print(pila.tamano())

elif opcion == 2:
    class Cola:
        def __init__(self):
            self.items = []

        def estaVacia(self):
            return self.items == []

        def agregar(self, item):
            self.items.insert(0,item)

        def avanzar(self):
            return self.items.pop()

        def tamano(self):
            return len(self.items)

    cola = Cola()
    print(cola.estaVacia())
    cola.agregar(4)
    cola.agregar('perro')
    cola.agregar(True)
    print(cola.tamano())
    print(cola.estaVacia())
    cola.agregar(8.4)
    print(cola.avanzar())
    print(cola.avanzar())
    print(cola.tamano())

elif opcion == 3:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None

    class ListaEnlazada:
        def __init__(self):
            self.cabeza = None

        def estaVacia(self):
            return self.cabeza == None

        def agregar(self, valor):
            nuevo = Nodo(valor)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

        def tamano(self):
            actual = self.cabeza
            contador = 0
            while actual:
                contador = contador + 1
                actual = actual.siguiente
            return contador

        def buscar(self, valor):
            actual = self.cabeza
            while actual:
                if actual.valor == valor:
                    return True
                actual = actual.siguiente
            return False
"""