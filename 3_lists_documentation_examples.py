'''
Son un tipo de dato que nos permite manejar grandes cantidades de datos.
Este tipo de dato es similar a los arreglos con la diferencia de que en 
este caso las listas pueden cambiar de tamaño pueden crecer o decrecer, 
los arreglos no.

Son mutables: lo que significa que sus elementos pueden cambiar o reordenarse.

'''

# Creación de Listas --------------------------------------------------------------------------------------------

lista_vacia = []
print(f'Esto es una lista vacia:{lista_vacia}')
# Podemos verificar de que tipo es la variable lista_vacia
print('La variable lista_vacia es de tipo:', type(lista_vacia))

# Otra forma de crear una lista es usando la clase list()
nueva_lista = list()
print(f'Esto tambien es una lista vacia:{nueva_lista}')
# Podemos verificar de que tipo es la variable lista_vacia
print(f'La variable lista_vacia es de tipo:{type(nueva_lista)}')

# Si queremos definir una lista de frutas y otra de numeros por ejemplo podemos hacerlo de la siguiente forma:
frutas = ['naranja', 'manzana', 'banana', 'frutilla', 'arandanos']
numeros = [1, 3, 5, 7]

print(f'Lista de frutas: \n {frutas}')
print(f'Lista de numeros: \n {numeros}')

# Tambien podemos definir una lista que contenga una mezcla de tipos de datos, aunque no es tan comun ver esto
mezcla = [1.5, 'a', 5, True, [1,2,3]]
print(f'Lista mezclada: \n {mezcla}')

#----------------------------------------------------------------------------------------------------------------

# Acceder a elementos -------------------------------------------------------------------------------------------
#Supongamos que tenemos una lista de verduras
verduras = ['papa', 'cebolla', 'rucula', 'batata', 'lechuga']

# Las listas se manejan por medio de indices
# Los índices comienzan desde la posición 0 y la posición de finalización se calcula mediante la fórmula length-1
verduras = ['papa', 'cebolla', 'rucula', 'batata', 'lechuga']
#              0         1        2          3         4

# Esto quiere decir que si yo quiero acceder por ejemplo al contenido de la primera posicion 
# puedo hacerlo indicando el valor del indice o posicion de la que quiero conocer el valor
# En el ejemplo de la lista de verduras 'papa' tendria el indice 0, 'cebolla' el 1 .. y asi sucesivamente
# Para mostrar la primera posicion de una lista escribimos
una_verdura = verduras[0]
print(f'Esta es la primera posicion de la lista: {una_verdura}')

# Si colocamos un indice que esta fuera del rango de elementos obtendremos un error 'IndexError: list index out of range'
#Tambien podemos trabajar con indices negativos por ejemplo si usamos -1 accedemos a la última posición de la lista, 
# Si usamos -2 el penúltimo y así podemos recorrer la lista a la inversa

ultima_verdura = verduras[-1]
print(f'Esta es la ultima posicion de la lista:{ultima_verdura}')

#Las listas son mutables, es decir, podemos modificar los elementos que la componen
verduras = ['papa', 'cebolla', 'rucula', 'batata', 'lechuga']
#              1         2         3          4         5

print(f'Lista antes de modificar elemento: \n {verduras}')
verduras[0] = 'rabanito'
print(f'Lista despues de modificar elemento: \n {verduras}')

#Podemos obtener sublistas a partir de una lista, por ejemplo

cursos = ['Word', 'Excel', 'Access', 'Powerpoint', 'Illustrator', 'Photoshop', 'Corel Draw']
#           1         2        3          4             5               6           7

#Estas son dos formas de escribir que queremos los cursos desde la posicion 0 a la 2 
sub_cursos = cursos[0:3]
print(f'Los primeros tres cursos: \n {sub_cursos}')
sub_cursos = cursos[:3]
print(f'Los primeros tres cursos: \n {sub_cursos}')

#Si queremos obtener los valores desde una posición específica por ejemplo 5 entonces 
sub_lista_cursos = cursos[5:]
print(f'Los cursos a partir de la posicion 5: \n {sub_cursos}')

#Si no colocamos limites entonces obtendremos la lista completa
lista_cursos = cursos[:]
print(f'Los cursos de la lista son: \n {lista_cursos}')

#Tambien podemos obtener sublistas con saltos entre elementos
sub_cursos_saltos = cursos[1:5:2]
print(f'Los cursos con saltos de 2 en 2 son: \n {sub_cursos_saltos}')


# Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.
# [:] Todos los elementos.
# [start:] Todos los elementos desde el índice establecido(start).
# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
# [start:end] Todos los elementos de un rango de índices.
# [start:end:step] Todos los elementos de un rango de índices con saltos.


#----------------------------------------------------------------------------------------------------------------

# Como recorremos los elementos de una lista? -------------------------------------------------------------------
# Para recorrer los elementos de una lista vamos a utilizar la estructura 'for'

verduras = ['papa', 'cebolla', 'rucula', 'batata', 'lechuga']
for una_verdura in verduras:
    print(f'Verdura: \n {una_verdura}')

# Para mostrar la posicion y el valor de cada posicion recorro la lista usando dos indices
# Utilizo el metodo enumerate() para añadir un contador que me vaya mostrando la posicion en cada bucle
# La sintaxis de enumerate() es la siguiente: enumerate(iterable, start=0) donde 'iterable' es la lista sobre la que quiero iterar 
# y 'start' es opcional e indica a partir de que numero debo empezar a contar.

verduras = ['papa', 'cebolla', 'rucula', 'batata', 'lechuga']
for contador, una_verdura in enumerate(verduras):
    print(f'En la posicion {contador} esta una {una_verdura}')

# Para iterar por mas de una lista usando la funcion zip()
# A la funcion zip() le tengo que pasar como parametros las listas sobre las que quiero iterar
famosos = ['Mirtha Legrand', 'Marcelo Tinelli', 'Marley', 'Guillermo Francella', 'Adrian Suar']
edades = [95,55,45,65,55]

for famoso, edad in zip(famosos, edades):
    print(f'{famoso} tiene {edad} años de edad')

# Lunes 16 de noviembre 

#----------------------------------------------------------------------------------------------------------------

# Palabras reservadas in y not in para recorrer una lista -------------------------------------------------------
# in y not in devuelven un valor booleano y me permiten verificar si un elemento se encuentra o no en la lista
verduras = ['papa', 'cebolla', 'rucula', 'batata', 'lechuga']
# 'in' verifica que el elemento esté en la lista y devuelve verdadero o falso
print('rabanito' in verduras)  # no se encuentra entonces devuelve False
print('batata' in verduras)    # se encuentra entonces devuelve True

# 'not in' verifica que el elemento no esté en la lista y devuelve verdadero o falso
print('rabanito' not in verduras) # no se encuentra entonces devuelve True
print('batata' not in verduras)   # se encuentra entonces devuelve False

'''
Ejercicio 1:
Escribir un programa que pida al usuario una palabra y muestre 
por pantalla el número de veces que contiene cada vocal.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")


#----------------------------------------------------------------------------------------------------------------
# Algunos metodos importantes para uso de listas ----------------------------------------------------------------

# append() – Agrega un elemento al final de la lista ----------------
colores = ['azul', 'rojo', 'verde', 'amarillo']
print(f'Lista de colores antes de agregar elemento: \n {colores}')
colores.append('violeta')
print(f'Lista de colores despues de agregar elemento: \n {colores}')

#Tambien puedo agregar otra lista por ejemplo
colores = ['azul', 'rojo', 'amarillo']
print(f'Lista de colores antes de agregar elemento: \n {colores}')
colores_secundarios = ['verde', 'naranja', 'violeta']
colores.append(colores_secundarios)
print(f'Lista de colores despues de agregar elemento: \n {colores}')
#---------------------------------------------------------------------

# extend() – Agrega los elementos extendiendo la lista ---------------
colores = ['azul', 'rojo', 'amarillo']
print(f'Lista de colores: \n {colores}')
colores_secundarios = ['verde', 'naranja', 'violeta']
colores.extend(colores_secundarios)
print(f'Lista de colores extendida: \n {colores}')

#Otra forma de extender una lista puede ser concatenandolas
colores_extendidax = colores + colores_secundarios
print(f'Lista de colores extendida: \n {colores_extendidax}')
colores_extendida = colores + ['negro', 'blanco']
print(f'Lista de colores extendida: \n {colores_extendida}')

#---------------------------------------------------------------------

# insert() - Agrega elementos en una posicion especifica -------------
vocales = ['a', 'e', 'i', 'u']
print(f'Lista de vocales antes de agregar elemento: \n {vocales}')
# 'o' se va a colocar en el indice 3
vocales.insert(3, 'o')
print(f'Lista de vocales despues de agregar elemento: \n {vocales}')
#---------------------------------------------------------------------

# remove() - Elimina elementos en una posicion especifica ------------
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'Lista de vocales antes de eliminar elemento: \n {vocales}')
# 'o' se va a eliminar en el indice 3
vocales.remove('o')
print(f'Lista de vocales despues de eliminar elemento: \n {vocales}')
#---------------------------------------------------------------------

# del - Es una sentencia que me permite eliminar un elemento al pasarle la posicion en la que se encuentra
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'Lista de vocales antes de eliminar elemento: \n {vocales}')
# 'o' se va a eliminar en el indice 3
del vocales[3]
print(f'Lista de vocales despues de eliminar elemento: \n {vocales}')
#---------------------------------------------------------------------

# pop() – Remueve el ultimo elemento de una lista, si indico la posición remueve esa posición indicada

cursos = ['Word', 'Excel', 'Access', 'Powerpoint', 'Illustrator', 'Photoshop', 'Corel Draw']
#           0        1        2          3             4               5           6

print(f'Lista de cursos antes de eliminar elemento: \n {cursos}')
valor_a_eliminar = cursos.pop()
valor_a_eliminar = cursos.pop(3)
print(f'Lista de cursos despues de eliminar elemento en posicion 3: \n {cursos}')
#------------------------------------------------------------------------------------------------------

# count() - Indica cuantas veces se repite un elemento en una lista -----------------------------------

vocales = ['a', 'i', 'e', 'i', 'o', 'i', 'u']
# cuenta cantidad de veces que aparece 'i'
cuenta_vocales = vocales.count('i')
print(f'Cantidad de veces que aparece i: {cuenta_vocales}')
# cuenta cantidad de veces que aparece 'x'
cuenta_consonantes = vocales.count('x')
print(f'Cantidad de veces que aparece x: {cuenta_consonantes}')
#------------------------------------------------------------------------------------------------------

# reverse() – Devuelve el reverso de una lista --------------------------------------------------------

cursos = ['Word', 'Excel', 'Access', 'Powerpoint', 'Illustrator', 'Photoshop', 'Corel Draw']
#           0        1        2          3             4               5           6

print(f'Lista de cursos original: \n {cursos}')
cursos_inversa = cursos.reverse()
print(f'Lista de cursos inversa: \n {cursos_inversa}')
cursos_inversa = cursos[::-1] #sin usar metodo reverse()
print(f'Lista de cursos inversa: \n {cursos_inversa}')
#------------------------------------------------------------------------------------------------------

#copy() - Permite copiar una lista en otra sin cambiar la lista original ------------------------------
#Podemos copiar el contenido de una lista en otra nueva usando el operador =
#Pero al trabajar sobre las listas se modifican ambas, es por ello que es mejor usar el metodo copy()
una_lista = [1, 2, 3]
nueva_lista = una_lista
# Agrego un elemento a la lista
nueva_lista.append('a')

print('Nueva Lista:', nueva_lista)
print('Una List:', una_lista)

#El metodo copy() no recibe parametros
una_lista = [1, 2, 3]
nueva_lista = una_lista.copy()

nueva_lista.append('a')
print('Nueva Lista:', nueva_lista)
print('Una List:', una_lista)
#------------------------------------------------------------------------------------------------------


#sort() - Permite ordenar los elementos de una lista --------------------------------------------------
vocales = ['i', 'o', 'u', 'o', 'a']
print(f'Lista desordenada: \n {vocales}')
#Ascendente
vocales_ascendente = vocales.sort()
print(f'Lista ordenada ascendente: \n {vocales_ascendente}')
#Descendente
vocales_descendente = vocales.sort(reverse=True)
print(f'Lista ordenada descendente: \n {vocales_descendente}')
#------------------------------------------------------------------------------------------------------

#index() - Permite saber la posicion en la que se encuentra un valor especifico -----------------------
colores = ['azul', 'rojo', 'verde', 'amarillo']
print(f"Lista de colores: {colores}")
posicion_color = colores.index('rojo')
print(f"La posicion del color rojo es: {posicion_color}")
#------------------------------------------------------------------------------------------------------

# Algunas funciones importantes para uso de listas ----------------------------------------------------

#len() - Me permite saber la longitud de una lista, es decir, la cantidad de elementos que contiene
colores = ['azul', 'rojo', 'verde', 'amarillo']
size_colores = len(colores)
print(f'La longitud de la lista es: \n {size_colores}')
print(f'La longitud de la lista es: \n {len(colores)}')
#---------------------------------------------------------

#max() - obtener el maximo valor de una lista
numeros = [10,2500,15,500,1,1500]
maximo = max(numeros)
print(f'Mayor valor de la lista: \n {maximo}')
#---------------------------------------------------------

#min() - menor valor de la lista
numeros = [10,2500,15,500,1,1500]
menor = min(numeros)
print(f'Menor valor de la lista: \n {menor}')
#---------------------------------------------------------


#Ejercicios de Ejemplos 
# 1- Ingresar las notas de un alumno en una lista y al finalizar calcular el promedio ------------------------------------------
print("Bienvenido, a continuacion se le solicitara que ingrese notas del alumno \n")
lista_notas = []
ingresar = True

while ingresar:
    nota = float(input("Ingrese nota del alumno o ingrese '0' para finalizar: \n"))
    if nota == 0:
        ingresar = False
    else:
        #Agrego elemento al final de la lista usando metodo append()
        lista_notas.append(nota)

if lista_notas:
    #Para calcular el promedio uso las funciones sum() para sumar los elementos de la lista y len() para saber la longitud.
    promedio = sum(lista_notas)/len(lista_notas)
    print(f"El promedio de notas ingresadas es: {promedio} \n")
    print(f"Las notas ingresadas fueron: \n")
    for nota in lista_notas:
        print(nota)
else:
    print("No se ingresaron notas, el promedio es 0")

#------------------------------------------------------------------------------------------------------------------------------

# 2- Ingresar nombres de provincias en una lista, mostrar la lista cargada,
# luego solicitar que se ingrese nuevamente una provincia para eliminarla de la lista
print("Bienvenido, a continuacion se le solicitara que ingrese nombres de provincias \n")
# Carga de la lista
ingresar = True
provincias = []

while ingresar:
    nom_provincia = input("Ingrese una provincia o ingrese 'Salir' para finalizar: \n")
    if nom_provincia == 'Salir':
        ingresar = False
    else:
        provincias.append(nom_provincia)
print('---------------------------------------------------------------------------')
print('Provincias ingresadas: \n')
for provincia in provincias:
    print(provincia)

print('--------------------------------------------------------------------------- \n')

# Eliminacion de una sola provincia ingresada por el usuario
# Si quisiera eliminar mas de una provincia tendría que hacer un ciclo while como el que se hizo para la carga de la lista

borrar_provincia = input("Ingrese una provincia a eliminar: \n")
provincias.remove(borrar_provincia)
print(f"Esta es la lista: {provincias}, luego de eliminar la provincia: {borrar_provincia}")

# Ejemplo 3
'''
Ejercicio 2:
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible! Debe contener una o más palabras")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista.append(palabra)
    print("La lista creada es:", lista)

    buscar = input("Sustituir la palabra: ")
    sustituir = input("por la palabra: ")
    for i in range(len(lista)):
        if lista[i] == buscar:
            lista[i] = sustituir
    print("La lista es ahora:", lista)

