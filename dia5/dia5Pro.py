import random

##30
num=random.randint(1, 10)
print("adivine el número que estoy pensando, está entre 1 y 10, ingrese uno: ")
x=int(input())
while x!=num:
    print("ese no es, vaya otra vez: ")
    x=int(input())
print("ese es") 

