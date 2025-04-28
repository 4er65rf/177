# 10. Leer, escribir y modificar un archivo de texto.
with open("archivo.txt", "w") as archivo:
    archivo.write("Python es insoprtable.\n")
    archivo.write("Python es intendible.\n")
print ("Archivo creado con éxito")
