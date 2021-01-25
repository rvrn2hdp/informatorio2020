'''
 Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada,
 controle y sustituya cualquier elemento negativo por 0.
'''

miLista = []

while len(miLista) < 5:
    elemento = int(input("Ingrese un elemento: "))
    # append agrega un elemento al final de la lista
    miLista.append(elemento)

cont = 0
while cont < len(miLista):
    if miLista[cont] < 0:
        elemento = int(input("Ingrese un número positivo: "))
        miLista[cont] = elemento
    cont += 1
    
print(miLista)