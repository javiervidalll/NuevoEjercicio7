"""nombre y número de teléfono"""

listanombretelefono = []

while True:
    nombre = input("Escriba un nombre: ")
    if nombre == "fin":
        break
    telefono = input("Escribe el numero de a quien quieras llamar: ")
    linea = {}
    linea["Nombre"] = nombre

    linea["Teléfono"] = telefono

    listanombretelefono.append(linea)

for linea in listanombretelefono:
    print(linea)