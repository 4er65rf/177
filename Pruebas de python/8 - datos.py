
#Relacionales
#= igualdad
#!=,<> diferenciales
#>=,<= desigualdades
#<,> inecuación
#Lógicos
#Y and
#O or
#N not
#Aritméticos
#P  Parentesis ()
#E  Exponentees b^2 b**2
#M  *
#D  / -> // % 
#A  +
#S  -

#Tipos de datos basicos
str()
float()
int()

#Tipos de datos estructurados

set() #<-Conjunto
list() #<-Lista
tuple() #<-Tupla
dict() #<-Diccionario

conj = set([1,2,3])
print(conj,type(conj))
conj = {4,5,6}
print(conj,type(conj))

conj.add(1)
conj.add(2)
conj.add(3)
conj.add(4)

print(conj)


#Tipos de datos compuestos

#enumerate()
#range() 

Listota = list()

List = list([1,2,3])
Listota.append(List)
print(List,type(List))
List = [3,4,5]
Listota.append(List)
print(List,type(List))
Calif = [-1]*40

#for i in range (40):
  #  Calif.append(0)


ListaForInLine = [i for i in range(1,41)if i%5 == 0]
print(ListaForInLine,type(ListaForInLine))               


Listota.append(Calif)
print(Calif,type(Calif))

print(Listota)



tuplas = tuple()
print(tuplas,type(tuplas))
tuplas = ( )
print(tuplas,type(tuplas))


import math

segundosAnio = (60,60,24,365)

#segundosAnio[3] = 365.25  #no se puede hacer


segundos = math.prod([segundosAnio [i] for i in range(len(segundosAnio))])


print(segundos)

#Diccionarios
alumnos = dict()
print(alumnos,type(alumnos))
alumnos ={2045337:"Jesús", 32433: "Rfael Juarez Bernal"}
print(alumnos,type(alumnos))


print(alumnos[2064462])
print(alumnos[2111834])

alumnos[1484412]="Luis Angel Gutierrez"
print(alumnos,type(alumnos))
print(alumnos[1484412])

alumnos['Fimeno']= "ING. PANCHO PEREZ"
print(alumnos['Fimeno'])



for item in enumerate (segundosAnio,100):
    print(item)


for i in range(0,43,6):
    print(i)


for i in [0,6,12,18,24,30,36,42]:
    print(i)


for i in range(0,151,15):
    print(i/10)