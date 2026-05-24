# -------------------

def limpiar():
    print("\033c")

# -------------------

def calcular_ventas(respuesta, cantidad_autos, total_ventas):
    limpiar()

    while respuesta == "S":

        marca_auto = input("Marca: ").strip().upper()
        pais = input("Origen: ").strip().upper()
        precio = float(input("Costo: "))

        porcentaje = 0

        if pais == "ALEMANIA":
            porcentaje = 0.20

        elif pais == "JAPON":
            porcentaje = 0.20

        elif pais == "ITALIA":
            porcentaje = 0.15

        elif pais == "USA":
            porcentaje = 0.08

        impuesto = precio * porcentaje
        precio_final = precio + impuesto

        print(f"El impuesto a pagar es: ${impuesto}")
        print(f"El precio de venta es: ${precio_final}")

        cantidad_autos += 1
        total_ventas += precio_final

        respuesta = input(
            "¿Deseas realizar otra vez el proceso (S/N): "
        ).upper().strip()

    return cantidad_autos, total_ventas

# -------------------

opcion = "S"
contador = 0
acumulador = 0

total_autos, suma_ventas = calcular_ventas(
    opcion,
    contador,
    acumulador
)

print(
    f"El total de vehículos ingresados es: {total_autos}"
    f"\nY el monto total de los precios de venta es: ${suma_ventas}"
)

# -------------------