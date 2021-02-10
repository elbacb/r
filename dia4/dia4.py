""" LISTAS """
""" 
añadir:
    .append()
    + 
borrar:
    .pop()

eliminar lista:
    del

vacear:
   .clear()

slice (trozo de lista)

longitud:
    len()
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