Limite= int(input("Ingresa un limite"))

par=[]  #estos dos son lo mismo
impar = list()

for num in range(1,Limite+1):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

impresion = max(len(par),len(impar))

for item in range(impresion):
    try:
        print(par[item], impar[item])
    except IndexError:
        try:
            v1=par[item]
        except IndexError:
            v1='-'
        try:
            v2=impar[item]
        except:
            v2='-'
        finally:
            print(v1, v2)
        
'''
for item in range(impresion):
    try:
        print(par[item], impar[item])
    except IndexError:
        try:
            v1=par[item]
        except IndexError:
            v1='-'
'''        

#print(par[item] if par[item] is not None else 0, impar[item] is not None else 0)

if True:
    print("Hola Mundo")

if False:
    print("Me van a brincar")
else:
    print("oook")

if None:
    print("Esto no seta ejecutado")
elif False:
    print("print")
else:
    print("Nada")
    