''' Desafío 3
 Realiza una función separar(lista) que tome una lista que tenga
 datos de cantidad de árboles plantados en diferentes ciudades de
 Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas.
 La primera con las cantidades que superen los 100 y la segunda con el resto.
 Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
'''
from random import randint

def separar(lista):
    listaMas100 = []
    listaMenos100 = []
    for cantidad in lista:
        if cantidad >= 100:
            listaMas100.append(cantidad)
        else:
            listaMenos100.append(cantidad)
    
    return listaMas100, listaMenos100

cantidad_arboles = []
for i in range(50):
    cantidad_arboles.append(randint(1, 200))

lista1, lista2 = separar(cantidad_arboles)

print(f"La cantidad de ciudades que plantaron mas de 100 arboles es {len(lista1)}")
print(f"La cantidad de ciudades que plantaron menos de 100 arboles es {len(lista2)}")
