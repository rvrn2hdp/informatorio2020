''' Realice una función que dada una lista de enteros L, y un número entero n.
 Elimine de la lista original los elementos que sean iguales a ese número dado.
'''
from random import randint

def eliminar_elementos(listaL, n):
    cont = 0
    while cont < len(listaL):
        if n == listaL[cont]:
            del listaL[cont]
        cont += 1

    return listaL

unaLista = list()
while len(unaLista) < 10:
    unaLista.append(randint(0,10))

print(unaLista)

numero = randint(0, 10)
print(numero)

print(eliminar_elementos(unaLista, numero))