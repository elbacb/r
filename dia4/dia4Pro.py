##24 imprime los >10
""" 
nums = [1, 23, 5, 8, 40, 12, 2, 67, 24, 9, 39]
for indice in range(len(nums)):
  if nums[indice]>10:
   print(nums[indice])
 """
""" # otra solucion
nums = [1, 23, 5, 8, 40, 12, 2, 67, 24, 9, 39]
for indice in nums:  
  if indice>10: print(indice)
 """  
##23 retorna último elemento de lista
""" 
def ulti(lita):
  if lita==[]:
    return "lista vacía"
  else:
    l=len(lita)
    return lita[l-1]
print(ulti([5, 1, 8, 7])) # 7
print(ulti([])) # "La lista está vacía"
 """

##22 ordena lista de números
## d es el índice o ubicación dentro de la lista, y va de 0 hasta longitud-1
""" 
def orde(lita):
  for d in range(len(lita)-1): #este for repite el otro for, l veces, donde l=longitud
    for d in range(len(lita)-1): #adentro de este for se intercambian pares contiguos
      if lita[d]>lita[d+1]:
        temp=lita[d]
        lita[d]=lita[d+1]
        lita[d+1]=temp
  return lita
print(orde([5,12,4,6,8,1,0,-1,3,12,15,17,-3]))
"""


#21 combinar dos listas en una nueva combinada en tuplas
""" 
def combina(lista1, lista2):
  combi=list(zip(lista1, lista2))
  return combi
print(combina([1, 2], ['a', 'b'])) # [(1, 'a'), (2, 'b')]
print(combina(["Pedro", "Maria"], [15, 22])) # [("Pedro", 15), ("Maria", 22)]
 """
#20 recibe lista devuelve longitud, una solución es casi que reutilizar len(lista)

#19
""" reciba un número y retorne una lista desde 1 hasta el número recibido"""
"""
def derango(digito):
  lita=[]
  for i in range(digito): #range(digito)<->range(0,digito): i en intervalo de 0 a digito
    lita.append(i+1)
  return lita
print(derango(8))
 """

#18 
""" insertar elemento e imprimir verticalmente """
""" 
nombres = ["Pedro", "Maria", "Pablo", "Diana"]
nombres.append("juanita limaña")
for j in nombres:
  print(j)
 """
##otra solucion
""" 
nombres = ["Pedro", "Maria", "Pablo", "Diana"]
nombres=nombres+["Pedrina"] # nombres+=["Pedrina"] 
for j in nombres:
  print(j)
 """
##solucion rudimentaria
""" nombres.append("Juan")
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3]);print(nombres[4]) """