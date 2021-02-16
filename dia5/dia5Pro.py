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
