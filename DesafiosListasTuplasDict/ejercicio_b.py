'''
 Haz un programa que almacene 5 elementos en una variable del tipo lista,
  la modiﬁque para que cada componente sea igual al cuadrado del componente
  original. El programa mostrara la lista resultante por pantalla.
'''

miLista = []

while len(miLista) < 5:
    elemento = int(input("Ingrese un elemento: "))
    # append agrega un elemento al final de la lista
    miLista.append(elemento)

print(miLista)

cont = 0
while cont < 5:
    miLista[cont] = miLista[cont] ** 2
    cont += 1
    
print(miLista)
