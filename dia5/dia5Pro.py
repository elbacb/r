#import random
from random import randint
##30 adivinar número
#num=random.randint(1, 10) #esta forma se usa con la linea 1 en vez de la 2

""" 
num=randint(1, 10)
print("adivine el número que estoy pensando, está entre 1 y 10, ingrese uno: ")
x=int(input())
while x!=num:
    print("ese no es, vaya otra vez: ")
    x=int(input())
print("ese es")
 """
##29 promedio
""" 
print("ingrese números a la lista, se devuelve su promedio")
lita=[]
def prom(l):
    m=''
    acum=0
    while m=='':
        p=float(input("número: "))
        acum+=p
        l=l+[p]
        m=input("¿otro número?, espiche entrar ")
    return acum/len(l)
print(prom(lita))
 """

##28 multiplicar lista
""" 
def mult(l,m):
    for k in range(len(l)):
        l[k]*=m
    return l
print(mult([8, 4, 7, 9], 2)) # [16, 8, 14, 18]
 """
""" 
def mult(l,m):
    l=[l[k]*m for k in range(len(l))]
    return l
print(mult([8, 4, 7, 9], 2)) # [16, 8, 14, 18]
 """ 

##27 funcion que recibe lista y devuelve su suma
""" 
def sum(lita):
    acum=0
    for e in range(len(lita)):
        acum+=lita[e]
    return acum

print(sum([1, 2, 3])) # 6
print(sum([5, 1, 8, 7])) # 21
print(sum([])) # 0
 """

##26 
#números pares del 1 al 100 con un ciclo

#impresión de pares
""" 
for n in range(1,100):
    if (n)%2==0:
        print(n)

#generación de lista con pares
#sublista=[var_temp for var_temp in lista if condicional]
l=[n for n in range(1,100) if n%2==0]
print(l)
 """

##25
#impresion 10 veces de una frase ingresada

frase=input("ingrese una frase: ")
"""
#con for:
for e in range(0,10):
    print(frase)
 """
#con while:
e=0
while e<10:
        print(frase)
        e+=1