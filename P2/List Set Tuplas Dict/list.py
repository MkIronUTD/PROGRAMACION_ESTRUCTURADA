import os
import time
"""
1. LIST (list)
Una lista guarda varios elementos en orden.

Características:

Ordenada
Modificable
Permite elementos repetidos
permite diferentes tipos de datos

Ejemplo: 

frutas = ["manzana", "pera", "uva", "uva"]
print(frutas)
Salida:
['manzana', 'pera', 'uva', 'uva']

Modificar elementos:

frutas[1] = "sandia"
print(frutas)

Salida:
['manzana', 'sandia', 'uva', 'uva']

Agregar elementos:
frutas.append("melon")
"""

#===============================
#        Visto en clase
#===============================

os.system("clear")

pasises = ["Mexico","Canada","EUA","Mexica","Brasil"]
numeros = [23,45,8,24]
varios = [33,3.1416,"Hola",True]
vacio = []

print(pasises)
print(numeros)
print(varios)
print(vacio)


time.sleep(3)
os.system("clear")

#recorrer lista uno por uno izquierda a derecha
for i in pasises:
    print (i)
    time.sleep(1)
    #Primera forma
    
os.system("clear")
for i in range(0,5):
    print(pasises[i])
    time.sleep(1)
    #Segunda forma
    
os.system("clear")
for i in range (0,len(pasises)):
    print(pasises[i])
    time.sleep(1)
    
#Ordenar elementos en una lista
print(pasises)
pasises.sort()
print(pasises)

#Agregar elementos a una lista
pasises.append("Honduras")
print(pasises)

#Segunda forma de agregar elementos
pasises.insert(1, "Colombia")
print(pasises)

#Eliminar 1ra forma
pasises.pop(3)
print(pasises)

#2nda forma
# pasises.remove("EUA")
# print(pasises)

#Buscar un elemento dentro de una lista
encontro = "Mexico" in pasises
print(encontro)

#Contar el numero de veces que aparece un elemento en la lista
num_veces=numeros.count(23)
print(f"El valor 23 aparece {num_veces} veces")

#Conocer la posicion de un elemento en lista
for i in range(0,len(pasises)):
    if pasises[i] == "Mexico":
        posicion =i
        print(f"Encontre el valor en la posicion {posicion}")
        
#Unir el contenido de una lista a otra
numeros2 =[100,-100]
print(f"{numeros} {numeros2}")
numeros.extend(numeros2)
print(numeros)

#Mostrar descendentemente
print(numeros.reverse)