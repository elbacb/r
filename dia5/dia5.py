""" print(list(range(9)))
 """

##break
"""
razas =["pug", "beagle", "aleman", "chandoso", "criollo"]
for perro in razas:
    print(perro)
    if perro=='aleman':
        print("aleman encontrado")
        break
 """
##continue
""" 
nume=[3, -17, 6.4, -11.4, 23, 8, 0, -11]
for n in nume:
    if n>0:
        continue
    print(n)
 """
##ciclos concatenados (nested)

""" equipos =[['andres', 'juan'], ['pedro', 'santiago', 'juliana'], ['juan manuel']]

for equipo in equipos:
    print(equipo)
    for i in equipo:
        print(i)
 """

##while
""" 
razas =["pug", "beagle", "aleman", "chandoso", "criollo"]

inicializador=0
while inicializador<len(razas):
    print(razas[inicializador])
    inicializador+=1
 """
##compresiones de listas (list comprehensions)
##ciclo for dentro de una lista para obtener otra LISTA
razas =["pug", "beagle", "aleman", "chandoso", "criollo"]

""" 
beagles=[]
for raza in razas:
    if raza=='beagle':
        beagles.append('beagle'*3) ##*3 imprime tres veces la cadena
print(beagles)
 """
""" 
beagles=[]
for raza in razas:
    if raza=='beagle':
        beagles.append('beagle')
print(beagles)
 """
#5 lineas anteriores equivalen a las dos siguientes, mismo resultado
beagles=[raza for raza in razas if raza == 'beagle']
print(beagles)
#beagle=[var_temp for var_temp in lista if condicional]

#sirve sin condicional en este caso:
""" 
beagles =[raza for raza in razas] 
print(beagles) 
 """

#imprime usuarios que empiezan por @

""" 
palabras=["@pepe", "#sinfiltro", "@nombre", "@zezeo", "nomas" ]
nomusu=[palabra for palabra in palabras if palabra[0]=="@"]
print(nomusu)

mensajes=[usuario+' por favor sígame bueno' for usuario in nomusu ]
print(mensajes)
 """
#actualizacion de votos
misvotos=[23, 34, 12, 54, 12, 76, 27, 72]
votoshoy=[ voto + 100 for voto in misvotos ]
print(votoshoy)