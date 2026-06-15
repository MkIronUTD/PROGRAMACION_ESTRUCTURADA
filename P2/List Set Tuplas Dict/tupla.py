""""
Las tuplas se utilizan para almacenar varios elementos en una sola variable 

una tupla es una coleccion ordenada e inmutable 

las tuplas se escriben entre poarenntesis
"""

paises=("Mexico", "Canada", "EUA")
varios=("Hola", True, 33, 33.1416)

print(paises)

for i in paises:
    print(i)

print(f"El pais que inaugura la copa del mundo 2026 es: {paises[0]}")

for i in range(0, len(paises)):
    print(paises[i])
    

contador = 0
while contador < len(paises):
    print(paises[contador])
    contador+=1
    
edades=(23,24,18,20,20,23,24,19,24)

print(edades.count(24))

entrada = int(input("ingresa un numero: ").strip())
nveces = 0
for i in range (0,len(edades)):
    if edades[i] == entrada:
        print(f"El numero {entrada} esta en la posicion {i}")
        nveces+=1

print(nveces)


