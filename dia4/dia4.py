""" LISTAS """
""" añadir con
    .append()
    + 
borrar
    .pop()

eliminar lista
    del lista

vacear
   .clear()

slice (trozo de lista)

longitud
    len()
    
    """
ejemplos = ["rojo", "blanco", "verde", "azul"]
for color in range(len(ejemplos)):
    print(ejemplos(color))

""" zip (es un objeto) para emparejar"""
altura=[130, 145, 187, 175, 156]
nombre =["dani", "ricardo", "juan", "carla"]
print(list(zip(altura, nombre)))