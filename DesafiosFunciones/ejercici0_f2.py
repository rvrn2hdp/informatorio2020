'''Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas
    de dos ciudades se cumpla lo siguiente:
    Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
    Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
    Si ambos números son iguales, debe devolver el nombre de ambas.
'''

def relacion(a, b):
    if a > b:
        return ciudad1
    elif b > a:
        return ciudad2
    elif a == b:
        return ciudad1, ciudad2
    else:
        print("ERROR")
        return 

print("Ingrese el nombre de las ciudades:")
ciudad1 = input("Primer Ciudad: ")
ciudad2 = input("Segunda Ciudad: ")
print("¿Cuántas toneladas tiene cada ciudad?")
toneladas1 = float(input("Ingrese las toneladas de la primer ciudad: "))
toneladas2 = float(input("Ingrese las toneladas de la segunda ciudad: "))

if toneladas1 != toneladas2:
    print("La ciudad que mas toneladas recicladas tiene es:", relacion(toneladas1, toneladas2))
else:
    print("Las dos ciudades tienen la misma cantidad de basura.")