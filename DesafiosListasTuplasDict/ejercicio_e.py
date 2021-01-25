from copy import copy

'''
    Cargar m elementos en una pila, y luego copiarlos en una nueva lista.
'''

pila = []
while True:
    m = input("Ingrese un elemento a la pila: ")
    pila.append(m)
    seguir = input("¿Seguir agregando? (s/n): ")
    if seguir == 'n':
        break

lista_nueva = copy(pila)

for i in lista_nueva:
    print(i)