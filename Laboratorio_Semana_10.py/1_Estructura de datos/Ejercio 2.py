#Ejercicio 2: Manejo de Inventario con Listas y Diccionarios

#Ejemplo de entrada:
# 1. Agregar producto: Nombre: "Laptop", Categoría: "Electrónica", Precio: 1200.50, Cantidad: 5
# 2. Agregar producto: Nombre: "Silla", Categoría: "Muebles", Precio: 150.75, Cantidad: 10
# 3. Buscar producto: Nombre: "Laptop"
# 4. Mostrar inventario ordenado por precio
# 5. Eliminar producto: Nombre: "Silla"
# 6. Mostrar inventario ordenado por precio
# 7. Salir



def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    inventario[nombre] = {'categoria': categoria, 'precio': precio, 'cantidad': cantidad}
    print(f"Producto '{nombre}' agregado al inventario.")
    


def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Producto encontrado: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


def mostrar_inventario_ordenado(inventario):
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]['precio'])
    print("Productos ordenados por precio (menor a mayor):")
    for nombre, producto in productos_ordenados:
        print(f"Nombre: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def main():
    inventario = {}
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar inventario ordenado por precio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            eliminar_producto(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario_ordenado(inventario)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
    
#Fin del ejercicio 2
#El programa permite al usuario gestionar un inventario de productos, incluyendo agregar, eliminar, buscar y mostrar productos ordenados por precio.


#lambda se utiliza para definir una función anónima que se utiliza como clave para ordenar los productos por precio.
#sorted() se utiliza para ordenar los productos en función de su precio.
#key=lambda x: x[1]['precio'] se utiliza para especificar que la clave de ordenación es el precio del producto.
#float() convierte el precio ingresado a un número decimal.