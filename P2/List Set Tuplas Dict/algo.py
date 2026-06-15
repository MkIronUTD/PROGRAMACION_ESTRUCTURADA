def imc(peso,altura):
    resultado = peso / (altura**2)
    return resultado

n = 1

while n ==1:
    peso = float(input("Ingresa tu peso en kg"))
    altura =float(input("Ingresa tu altura en m"))
    
    resultado = imc(peso,altura)
    print(f"El resultado es = {resultado}")
    
    n = int(input("Desea repetir el programa si(1) no (0)"))