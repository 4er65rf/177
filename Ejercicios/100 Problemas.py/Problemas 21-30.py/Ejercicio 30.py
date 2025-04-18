#30. Implementar funciones recursivas.

# a) Sumar los elementos de una lista.
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])
    
# b) Calcular el factorial de un número.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

# c) Calcular la serie de Fibonacci de un número.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
