#Ejercicio 6: Sistema de GestiOn de Vehículos
 
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: {self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, num_puertas):
        super().__init__(marca, modelo, año, precio)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.num_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrica = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Motocicleta: {self.cilindrica} cc")


#Ejemplo de uso:
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 20000)
vehiculo1.mostrar_info()
print()

automovil1 = Automovil("Honda", "Civic", 2021, 25000, 4)
automovil1.mostrar_info()
print()

#super() llama al constructor de la clase padre
#__ _init__ _ _ llama al constructor de la clase padre
#self.marca = marca asigna el valor de la variable marca al atributo marca de la clase padre
#class Automovil(Vehiculo) hereda de la clase Vehiculo
#class Motocicleta(Vehiculo) hereda de la clase Vehicul

#Ejemplo de un sistema de gestión de vehículos utilizando clases y herencia en Python.
#Definimos una clase base llamada Vehiculo que tiene atributos comunes a todos los vehículos, como marca, modelo, año y precio.
#Luego, definimos dos clases derivadas: Automovil y Motocicleta, que heredan de la clase Vehiculo y añaden atributos específicos para cada tipo de vehículo.
#Finalmente, creamos instancias de cada clase y mostramos su información.