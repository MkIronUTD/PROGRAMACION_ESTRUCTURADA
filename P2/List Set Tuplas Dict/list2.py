#Crear una lista
numeros=[23,33,45,8,24,0,100]
print(numeros)

cadena=""
for i in numeros:
    cadena+=f"{i}"
    
print("["+cadena+"]")

cadena=""
for i in range(0,len(numeros)):
    cadena+=f"{numeros[i]}"
print("["+cadena+"]")
    
contador = 0
cadena=""
while contador <len(numeros):
    cadena+=f"{numeros[contador]}"
    contador+=1
print("["+cadena+"]")

#Ejemplo numero 2 

#Primera forma

# palabras = ["UTD","tercer","cuatrimestre","TI"]
# palabra=input("Dame la palabra a buscar:").strip()

# if palabra in palabras:
#     print(f"Encontre la palabra {palabra} en la lista")
# else:
#     print("No encontre la palabra en la lista")

#2nda forma
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar:").strip()

encontro=False
for i in palabras:
    if i == palabra:
        encontro = True
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra}")