# -------------------

print("\033c")

numero = int(input("Ingresa un número: "))

tabla = (
    f"{numero} x 1 = {numero*1}\n"
    f"{numero} x 2 = {numero*2}\n"
    f"{numero} x 3 = {numero*3}\n"
    f"{numero} x 4 = {numero*4}\n"
    f"{numero} x 5 = {numero*5}\n"
    f"{numero} x 6 = {numero*6}\n"
    f"{numero} x 7 = {numero*7}\n"
    f"{numero} x 8 = {numero*8}\n"
    f"{numero} x 9 = {numero*9}\n"
    f"{numero} x 10 = {numero*10}"
)

print(tabla)

# -------------------

numero = int(input("\nIngresa un número: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")

# -------------------

numero = int(input("\nIngresa un número: "))

for valor in range(100, 0, -10):
    resultado = numero * valor
    print(f"{numero} x {valor} = {resultado}")

# -------------------

numero = int(input("\nIngresa un número: "))

contador = 100

while contador > 0:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")

    contador -= 10

# -------------------

def multiplicar(valor1, valor2):
    respuesta = valor1 * valor2
    return respuesta


numero = int(input("\nIngresa un número: "))

tabla = (
    f"{numero} x 1 = {multiplicar(numero,1)}\n"
    f"{numero} x 2 = {multiplicar(numero,2)}\n"
    f"{numero} x 3 = {multiplicar(numero,3)}\n"
    f"{numero} x 4 = {multiplicar(numero,4)}\n"
    f"{numero} x 5 = {multiplicar(numero,5)}\n"
    f"{numero} x 6 = {multiplicar(numero,6)}\n"
    f"{numero} x 7 = {multiplicar(numero,7)}\n"
    f"{numero} x 8 = {multiplicar(numero,8)}\n"
    f"{numero} x 9 = {multiplicar(numero,9)}\n"
    f"{numero} x 10 = {multiplicar(numero,10)}"
)

print(tabla)

# -------------------

def multiplicar(valor1, valor2):
    respuesta = valor1 * valor2
    return respuesta


numero = int(input("\nIngresa un número: "))

for indice in range(1, 11):
    print(f"{numero} x {indice} = {multiplicar(numero, indice)}")

# -------------------