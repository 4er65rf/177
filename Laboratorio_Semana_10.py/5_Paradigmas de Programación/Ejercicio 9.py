#Ejercicio 9: Implementación de Múltiples Paradigmas


#Imperativa: Uso de estructuras de control como condicionales y bucles.
def imperativa():
    # Ejemplo de programación imperativa
    suma = 0
    for i in range(1, 11): #rago es una función que genera una secuencia de números, for es un bucle que itera sobre cada número en la secuencia
        suma += i
    print("Suma de los primeros 10 números:", suma)

#Estructurada: Separar el código en funciones bien definidas.
def estructurada():
    # Ejemplo de programación estructurada
    def suma(a, b): #suma es una función que toma dos argumentos y devuelve su suma
        return a + b #return es una instrucción que devuelve un valor de una función

    resultado = suma(5, 10)
    print("Resultado de la suma:", resultado)


#Modular: Crear diferentes módulos para funcionalidades específicas.
def modular():
    # Ejemplo de programación modular
    def multiplicar(a, b):
        return a * b

    resultado = multiplicar(5, 10)
    print("Resultado de la multiplicación:", resultado)
    

#Orientada a Objetos: Definir clases y objetos.
def orientada_a_objetos():
    # Ejemplo de programación orientada a objetos
    class Persona: #clase es una plantilla para crear objetos, define atributos y métodos
        def __init__(self, nombre): #__init__ es un método especial que se llama al crear un objeto, self es una referencia al objeto actual
            self.nombre = nombre #self.nombre es un atributo de la clase, se asigna el valor del argumento nombre al atributo nombre del objeto

        def saludar(self):
            print("Hola, mi nombre es", self.nombre)

    persona = Persona("Juan")
    persona.saludar()
