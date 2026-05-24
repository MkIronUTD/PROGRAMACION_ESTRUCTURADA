# -------------------

def procedimiento():
    nom = input("Ingrese su nombre:\n").upper().strip()
    ape = input("Ingrese sus apellidos:\n").upper().strip()

    print(f"El nombre del alumno es: {nom} {ape}")

# -------------------

def mostrar_datos(nombre, apellido):
    nom = nombre
    ape = apellido

    print(f"El nombre del alumno es: {nom} {ape}")

# -------------------

def capturar_datos():
    nom = input("Ingrese su nombre:\n").upper().strip()
    ape = input("Ingrese sus apellidos:\n").upper().strip()

    return nom, ape

# -------------------

def devolver_datos(nombre, apellido):
    nom = nombre
    ape = apellido

    return nom, ape

# -------------------

procedimiento()

nombre = input("Ingrese su nombre:\n").upper().strip()
apellidos = input("Ingrese sus apellidos:\n").upper().strip()

mostrar_datos(nombre, apellidos)

nombre, apellidos = capturar_datos()

print(f"El nombre del alumno es: {nombre} {apellidos}")

nom = input("Ingrese su nombre:\n").upper().strip()
ape = input("Ingrese sus apellidos:\n").upper().strip()

nombre, apellidos = devolver_datos(nom, ape)

print(f"El nombre del alumno es: {nombre} {apellidos}")

# -------------------