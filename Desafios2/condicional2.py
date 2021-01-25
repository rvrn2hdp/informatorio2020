""" Desarrolle un programa que permita determinar
    si un número X ingresado es par o impar.
"""
def verificar_entero():
    while True:
        try:
            numero = int(input("Escribe un numero: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if numero < 0:
            print("Debes escribir un número positivo.")
            continue
        else:
            break
    return numero

numero = verificar_entero()

if numero % 2 == 0:
    print("el numero es par.")
else:
    print("el numero es impar.")