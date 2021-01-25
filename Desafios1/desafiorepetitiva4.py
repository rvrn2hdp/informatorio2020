""" Desafio 4 - estructuras repetitivas:
 Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco)
 de acuerdo al tamaño indicado.
"""
print("modulo que simula crear un tablero...")

tamanio_filas = int(input("Ingrese las filas que tendrá el tablero: "))
# columnas = int(input("Ingrese las columnas que tendrá el tablero: "))
# tablero = [[None], [None]]

filas = list()
filas = [0] * tamanio_filas

cont1 = 1
for i in filas:
    cont2 = 1
    for j in filas:
        if (cont1+1) % 2 == 0:
            if (cont2+1) % 2 == 0:
                print("|V|", end='')
            else:
                print("|B|", end='')
        else:
            if cont1 % 2 == 0 and cont2 % 2 == 0:
                print("|V|", end='')
            else:
                print("|B|", end='')
        cont2 += 1
    print(" ")
    cont1 += 1
