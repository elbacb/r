## DICCIONARIOS
#llave(clave):valor
#llave solo puede ser int, bool o str
#en listas son índices, en diccionarios son llaves

""" 
#inicializar un diccionario
dicc={}
#alternativa
#dicc=dict{}

menu={"avena": 4, "galleta": 6, "chocolate": 23, "pan": 3}
print(menu["avena"])
menu["empanada"]=7

dicc.update({False: "Chapinero"})
print(dicc)

#listas o diccionarios como valor dentro del diccionario
menu={"avena": 4, "galleta": [6,11], "chocolate": 23, "pan": 3}
print(menu)
 """

universidad={"alumnos": ["ana", "juan", "maria"],
                "edades": [23, 25, 21],
                "promedio": 
                {"cálculo":1.5,"estadística": 3.7,"mecánica": 3.3}}
print(universidad)

#formas de iterar sobre diccionarios
for key, valor in universidad.items():
    print("esta es la llave", key)
    print("esta es el valor:", valor)

for key in universidad:
        print("esta es la llave:", key)

for key in universidad:
        print("esta es el valor:", universidad[key])
