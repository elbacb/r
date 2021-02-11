""" LISTAS """
""" 
añadir:
    lista.append(elemento)
    lista.insert()
    + 
borrar:
    lista.pop()

eliminar lista:
    del

vacear:
   lista.clear()

slice (trozo de lista):
    lista=[5,12,4,6,8,1,0,-1,3,12,15,17,-3]
    sublista=[3,len(lista)-1]
    sublista1=[3:]
    sublista2=[-3:]
    sublista3=[:-3]
    print(sublista)

longitud:
    len(lista)
"""

"""
ejemplos = ["rojo", "blanco", "verde", "azul"]
 r=range(len(ejemplos)) #es de tipo rango
l=list(r) #crea lista a partir de r
print(l)
print(type(l)) #l!=r, son datos de tipo diferente
 """

#imprime los índices
ejemplo = ["rojo", "amarillo", "verde", "azul"]
for color in range(len(ejemplo)):
    print(color)

#imprime los elementos
ejemplo1 = ["rojo", "blanco", "verde", "azul"]
for color in range(len(ejemplo1)):
    print(ejemplo1[color])




""" zip (es un objeto) para emparejar"""
""" altura=[130, 145, 187, 175, 156]
nombre =["dani", "ricardo", "juan", "carla"]
print(list(zip(altura, nombre))) """