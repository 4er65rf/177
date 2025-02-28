#Programa original de la formula general
#Autor: Valeria,Abby, Jesús
#Fecha: 27/02/2025
"""
a=(float(input(Ingrese el valor de a: )))
b=(float(input(Ingrese el valor de b: )))
c=(float(input(Ingrese el valor de cb: )))
def Disc (a,b,c)
d=(float(-b**2-(a*a*c)))
return d
def chicharronera (a,b,c):
    x1=((-b+Disc**0.5)/2a)
    x2=((-b-Disc**0.5)/2a)
return (x1,x2)
if disc>=0:
    print(chicharronera (a,b,c))
else
    x1=complex(-b/2a+(disc*-1j))
    x2=complex(-b/2a-(disc*-1j))
"""
#Programa corregido de la formula general
#Autor: Valeria,Abby, Jesús
#Fecha: 28/02/2025


print("Este programa calcula la formula general de una ecuación cuadrática")


a = float(input("Ingrese el valor de término cuadrático: "))


b = float(input("Ingrese el valor de término lineal: "))


c = float(input("Ingrese el valor de término independiente: "))


def Disc(a,b,c):


    d = float(-b**2-(4*a*c))


    return d


def chicharronera(a,b,c):


    x1 = (-b+Disc(a,b,c)**0.5)/(2*a)


    x2 = (-b-Disc(a,b,c)**0.5)/(2*a)


    return (x1,x2)


if Disc(a,b,c)>=0:


    print(chicharronera(a,b,c))


else:


    x1 = complex(-b/(2*a)+(Disc(a,b,c)*-1j))


    x2 = complex(-b/(2*a)-(Disc(a,b,c)*-1j))


    print(x1)


    print(x2)   




