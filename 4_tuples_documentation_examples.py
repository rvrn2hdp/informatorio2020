'''
Son un tipo de dato que nos permiten almacenar distintos tipos de datos, 
incluyendo listas y otras tuplas. La principal diferencia entre las listas 
y las tuplas es que las tuplas son inmutables, es decir, no podemos modificar 
los valores que almacena no podemos agregar o quitar elementos. Las tuplas son 
mucho mas rápidas a la hora de obtener los valores que contiene.
Ventajas:

- Generalmente usamos tuplas para tipos de datos heterogéneos (diferentes) 
y listas para tipos de datos homogéneos (similares).
- Como las tuplas son inmutables, iterar a través de una tupla es más rápido 
que con la lista. Por lo tanto, hay un ligero aumento del rendimiento.
- Las tuplas que contienen elementos inmutables se pueden usar como clave para 
un diccionario. Con listas, esto no es posible.
- Si tiene datos que no cambian, su implementación como tupla garantizará 
que permanezca protegida contra escritura.

'''

# Creación de Tuplas --------------------------------------------------------------------------------------------
tupla_vacia = ()
print(f'Esto es una tupla vacia:{tupla_vacia}')
#Podemos verificar de que tipo es la variable tupla_vacia
print(f'La variable tupla_vacia es de tipo:{type(tupla_vacia)}')

#Otra forma de crear una tupla es usando la clase tuple()
nueva_tupla = tuple()
print(f'Esto tambien es una tupla vacia:{nueva_tupla}')
#Podemos verificar de que tipo es la variable tupla_vacia
print(f'La variable tupla_vacia es de tipo:{type(nueva_tupla)}')

#Si queremos definir una tupla de dias y otra de numeros por ejemplo podemos hacerlo de la siguiente forma:
dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
numeros = (1, 3, 5, 7)

print(f'Tupla de dias: \n {dias}')
print(f'Tupla de numeros: \n {numeros}')

# Si definimos una tupla de esta forma se denomina "Empaquetado de tuplas"
dias = 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'
numeros = 1, 3, 5, 7
# Tambien podemos hacer un "Desempaquetado de tuplas" de la siguiente forma:
t = 12345, 54321, '¡hola!'
x, y, z = t
# El desempaquetado de tuplas requiere que el número de variables sea 
# igual al número de elementos de la tupla. 
# Observa que la asignación múltiple sólo es un efecto combinado del 
# empaquetado de tuplas y desempaquetado de secuencias.
# Esto resulta un poco asimétrico, ya que el empaquetado de varios valores siempre 
# resulta en una tupla, aunque el desempaquetado funciona para cualquier secuencia.

'''
En el caso que asignemos mas variables de las que tiene la tupla nos va a dar el siguiente error:
>>> m,n = d
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: too many values to unpack
>>> m,n,o,p=d
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: need more than 3 values to unpack
Podemos solucionarlo colocando un asterisco '*' delante de cualquiera de las variables
'''



#Tambien podemos definir una tupla que contenga una mezcla de tipos de datos, aunque no es tan comun ver esto
mezcla = (1.5, 'a', 5, True, (1,2,3), ['a','b','c'])
print(f'Tupla mezclada: \n {mezcla}')

#----------------------------------------------------------------------------------------------------------------

# Acceder a elementos -------------------------------------------------------------------------------------------
# Las tuplas se manejan por medio de indices al igual que las listas
# Los índices comienzan desde la posición 0 y la posición de finalización se calcula mediante la fórmula length-1
dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
#          0         1          2          3          4          5          6          

# Esto quiere decir que si yo quiero acceder por ejemplo al contenido de la primera posicion 
# puedo hacerlo indicando el valor del indice o posicion de la que quiero conocer el valor
# En el ejemplo de la tupla de dias 'Lunes' tiene el indice 0, 'Martes' el 1 .. y asi sucesivamente
# Para mostrar la primera posicion de una tupla escribimos
un_dia = dias[0]
print(f'Esta es la primera posicion de la tupla: {un_dia}')

#Si colocamos un indice que esta fuera del rango de elementos obtendremos un error 'IndexError: list index out of range'
#Tambien podemos trabajar con indices negativos por ejemplo si usamos -1 accedemos a la última posición de la tupla, 
# si usamos -2 el penúltimo y así podemos recorrer la tupla a la inversa

ultimo_dia = dias[-1]
print(f'Este es el ultimo dia de la tupla:{ultimo_dia}')

#Que pasa si tenemos tuplas anidadas? Como utilizamos los indices?
mix = ('perro', 'gato', 'gallina', ('canario','loro','guacamayo'), ['león','puma','yaguareté'])
mix_anidado_simple = mix[1][3]          #Devuelve la letra 'o' de gato
mix_anidado_complex = mix[3][1]         #Devuelve la palabra 'loro' de la tupla
mix_anidado_complexx = mix[4][2]        #Devuelve la palabra 'yaguarete' de la tupla
print(mix_anidado_simple)
print(mix_anidado_complex)
print(mix_anidado_complexx)


#Tambien podemos obtener subtuplas a partir de tuplas de la misma forma que con listas
cursos = ('Word', 'Excel', 'Access', 'Powerpoint', 'Illustrator', 'Photoshop', 'Corel Draw')
#           1         2        3          4             5               6           7

#Estas son dos formas de escribir que queremos los cursos desde la posicion 0 a la 2 
sub_cursos = cursos[0:3]
print(f'Los primeros tres cursos: \n {sub_cursos}')
sub_cursos = cursos[:3]
print(f'Los primeros tres cursos: \n {sub_cursos}')

#Si queremos obtener los valores desde una posición específica por ejemplo 5 entonces 
sub_tuplas_cursos = cursos[5:]
print(f'Los cursos a partir de la posicion 5: \n {sub_cursos}')

#Si no colocamos limites entonces obtendremos la tupla completa
tuplas_cursos = cursos[:]
print(f'Los cursos de la tupla son: \n {tuplas_cursos}')

#Tambien podemos obtener subtuplass con saltos entre elementos
sub_cursos_saltos = cursos[1:5:2]
print(f'Los cursos con saltos de 2 en 2 son: \n {sub_cursos_saltos}')


# Estas son las formas en las cuales podemos crear una nueva tupla (subtuplas) a partir de otra.
# [:] Todos los elementos.
# [start:] Todos los elementos desde el índice establecido(start).
# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
# [start:end] Todos los elementos de un rango de índices.
# [start:end:step] Todos los elementos de un rango de índices con saltos.

#----------------------------------------------------------------------------------------------------------------

# Como recorremos los elementos de una tupla? -------------------------------------------------------------------
# Para recorrer los elementos de una tupla vamos a utilizar la estructura 'for'

verduras = ('papa', 'cebolla', 'rucula', 'batata', 'lechuga')
for una_verdura in verduras:
    print(f'Verdura: \n {una_verdura}')

# Para mostrar la posicion y el valor de cada posicion recorro la tupla usando dos indices
# Utilizo el metodo enumerate() para añadir un contador que me vaya mostrando la posicion en cada bucle
# La sintaxis de enumerate() es la siguiente: enumerate(iterable, start=0) donde 'iterable' es la tupla sobre la que quiero iterar 
# y 'start' es opcional e indica a partir de que numero debo empezar a contar.

verduras = ('papa', 'cebolla', 'rucula', 'batata', 'lechuga')
for contador, una_verdura in enumerate(verduras):
    print(f'En la posicion {contador} esta una {una_verdura}')

# Para iterar por mas de una tupla usando la funcion zip()
# A la funcion zip() le tengo que pasar como parametros las tuplas sobre las que quiero iterar
famosos = ('Mirtha Legrand', 'Marcelo Tinelli', 'Marley', 'Guillermo Francella', 'Adrian Suar')
edades = (95,55,45,65,55)

for famoso, edad in zip(famosos, edades):
    print(f'{famoso} tiene {edad} años de edad')

#----------------------------------------------------------------------------------------------------------------

# Palabras reservadas in y not in para recorrer una tupla -------------------------------------------------------
# in y not in devuelven un valor booleano y me permiten verificar si un elemento se encuentra o no en la tupla
verduras = ('papa', 'cebolla', 'rucula', 'batata', 'lechuga')
# 'in' verifica que el elemento esté en la tupla y devuelve verdadero o falso
print('rabanito' in verduras)  # no se encuentra entonces devuelve False
print('batata' in verduras)    # se encuentra entonces devuelve True

# 'not in' verifica que el elemento no esté en la tupla y devuelve verdadero o falso
print('rabanito' not in verduras) # no se encuentra entonces devuelve True
print('batata' not in verduras)   # se encuentra entonces devuelve False

#----------------------------------------------------------------------------------------------------------------


# Algunos metodos importantes para uso de tuplas ----------------------------------------------------------------

#No puedo agregar elementos pero si puedo concatenar tuplas
colores = ('azul', 'rojo', 'amarillo') + ('verde', 'naranja', 'violeta')
print(f'Tupla de colores: \n {colores}')

# O puedo multiplicar los valores de una tupla
colores_multiplicado = (('azul', 'rojo', 'amarillo')*3)
print(f'Tupla de colores: \n {colores_multiplicado}')

#---------------------------------------------------------------------

# del - Es una sentencia que me permite eliminar un elemento al pasarle la posicion en la que se encuentra
vocales = ('a', 'e', 'i', 'o', 'u')
print(f'Tupla de vocales antes de eliminar elemento: \n {vocales}')
# 'o' se va a eliminar en el indice 3
del vocales[3]
del vocales
print(f'Tupla de vocales despues de eliminar elemento: \n {vocales}')
#---------------------------------------------------------------------

# count() - Indica cuantas veces se repite un elemento en una tupla -----------------------------------

vocales = ('a', 'i', 'e', 'i', 'o', 'i', 'u')
# cuenta cantidad de veces que aparece 'i'
cuenta_vocales = vocales.count('i')
print(f'Cantidad de veces que aparece i: {cuenta_vocales}')
# cuenta cantidad de veces que aparece 'x'
cuenta_consonantes = vocales.count('x')
print(f'Cantidad de veces que aparece x: {cuenta_consonantes}')
#------------------------------------------------------------------------------------------------------

# Reverso de una lista --------------------------------------------------------

cursos = ('Word', 'Excel', 'Access', 'Powerpoint', 'Illustrator', 'Photoshop', 'Corel Draw')
#           0        1        2          3             4               5           6

print(f'Tupla de cursos original: \n {cursos}')
cursos_inversa = cursos[::-1]                       #No puedo usar reverse, entonces lo hago sin usar metodo reverse()
print(f'Tupla de cursos inversa: \n {cursos_inversa}')
#------------------------------------------------------------------------------------------------------


#index() - Permite saber la posicion en la que se encuentra un valor especifico -----------------------
colores = ('azul', 'rojo', 'verde', 'amarillo')
print(f"Tupla de colores: {colores}")
posicion_color = colores.index('rojo')
print(f"La posicion del color rojo es: {posicion_color}")
#------------------------------------------------------------------------------------------------------

# Algunas funciones importantes para uso de Tuplas ----------------------------------------------------

#len() - Me permite saber la longitud de una tupla, es decir, la cantidad de elementos que contiene
colores = ('azul', 'rojo', 'verde', 'amarillo')
size_colores = len(colores)
print(f'La longitud de la tupla es: \n {size_colores}')
print(f'La longitud de la tupla es: \n {len(colores)}')
#---------------------------------------------------------

#max() - obtener el maximo valor de una tupla
numeros = [10,2500,15,500,1,1500]
maximo = max(numeros)
print(f'Mayor valor de la tupla: \n {maximo}')
#---------------------------------------------------------

#min() - menor valor de la tupla
numeros = [10,2500,15,500,1,1500]
menor = min(numeros)
print(f'Menor valor de la tupla: \n {menor}')
#---------------------------------------------------------

#zip() - nos devuelve un objeto que debemos convertir a tupla 
# donde vemos que se combina la tupla con la lista en tuplas.
tupla = (1,2,3,4,5,6)
lista = [10,20,30,40]

zipthis= zip(tupla, lista)

print(zipthis)
zipthis= tuple(zip(tupla, lista))

'''
Ejercicio:
Escribir un programa que indique si dos fichas de dominó encajan o no. 
Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5.
'''

set_ficha1=(3,5)
set_ficha2=(1,4)
encajan = False
ingreso_ficha1 = input('Ingrese valores de ficha 1 siguiendo el formato, por ejemplo: 2-4\n')
ingreso_ficha2 = input('Ingrese valores de ficha 2 siguiendo el formato, por ejemplo: 6-4\n')

ficha1 = ingreso_ficha1.split('-')
ficha2 = ingreso_ficha2.split('-')
#ficha1 = tuple(ingreso_ficha1.split('-'))
#ficha2 = tuple(ingreso_ficha2.split('-'))
print('La ficha 1 ingresada es:',ficha1)
print('La ficha 2 ingresada es:',ficha2)
for i in range(0,len(set_ficha1)):
    for j in range(0,len(set_ficha2)):
        if set_ficha1[i] == int(ficha1[i]) and set_ficha2[j] == int(ficha2[j]):
                #print('Las fichas encajan')
                encajan = True
        #else:
            #print('Las fichas no encajan')

if encajan:
    print('Las fichas encajan')
else: 
    print('Las fichas no encajan')



