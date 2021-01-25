hectareas = float(input("Ingrese el tamaño en hectareas: "))
matorral = input("¿Hay matorrales? S-SI | N-NO: ")
compuesto = float(input("Nivel de compuesto en el suelo"))

porcentaje = compuesto * 100 / hectareas

if porcentaje >= 10:
    print("Es factible usar fertilizantes.")
    