'''
Los diccionarios al igual que las listas y tuplas nos permiten almacenar distintos tipos 
de datos inclusive otros diccionarios. Son mutables, es decir que podemos agregar o quitar 
elementos de él y podemos modificar sus elementos. A diferencia de las listas y tuplas los 
diccionarios no se manejan por medio de índices sino que los valores que se almacenan en un 
diccionario en lugar de estar asociados a un índice están asociados a una llave(key) y cada 
llave debe tener un valor(vaue). El valor de una llave puede ser de cualquier valor u objeto en Python 
y es inmutable.
Un diccionario es entonces una colección de pares formados por una clave y un valor asociado a la clave.
Se construyen poniendo los pares(keys y values) entre llaves { } separados por comas, 
y separando la clave del valor con dos puntos :.
Se caracterizan por:
    - No tienen orden.
    - Pueden contener elementos de distintos tipos.
    - Son mutables, es decir, pueden alterarse durante la ejecución de un programa.
    - Las claves son únicas, es decir, no pueden repetirse en un mismo diccionario, y pueden ser de cualquier tipo de datos inmutable.
    - Si una clave se repite, se toma como valor el último valor declarado
'''

# Creación de Diccionarios --------------------------------------------------------------------------------------------
diccionario_vacio = ()
print(f'Esto es un diccionario vacio:{diccionario_vacio}')
#Podemos verificar de que tipo es la variable diccionario_vacio
print(f'La variable diccionario_vacio es de tipo:{type(diccionario_vacio)}')

#Otra forma de crear una tupla es usando la clase dict()
nuevo_diccionario = dict()
print(f'Esto tambien es un diccionario vacio:{nuevo_diccionario}')
#Podemos verificar de que tipo es la variable nuevo_diccionario
print(f'La variable nuevo_diccionario es de tipo:{type(nuevo_diccionario)}')

#Si queremos definir valores para un diccionario podemos hacerlo de la siguiente forma:
usuario = {
    'nombre': 'Juan Perez',
    'edad': 25,
    'curso': 'Programacion Web',
    'domicilio':{
        'calle':'Calle Falsa 123',
        'localidad': 'Saénz peña',
        'provincia': 'Chaco'
    },
    'nivel':'basico'
}


print(f'Estos son los datos de usuario, almacenados en un diccionario:{usuario}')
#Podemos almacenar anidar un diccionario dentro de otro por ejemplo:
dict_anidado = {
    'nombre_completo':{
        'nombre': 'Alfredo', 'Apellidos': 'Sánchez Alberca'
    }
}
print('Esto es un diccionario anidado:', dict_anidado)

#----------------------------------------------------------------------------------------------------------------

# Acceder a elementos -------------------------------------------------------------------------------------------
# Así como en las listas usabamos los índices para acceder a un elemento, en los diccionarios utilizaremos las claves
usuario = {
    'nombre': 'Juan Perez',
    'edad': 25,
    'curso': 'Programacion Web',
    'habilidades':{
        'programacion':'no',
        'base de datos':'si'
    },
    'nivel':'basico'
}
#d[clave] devuelve el valor del diccionario d asociado a la clave clave. 
# Si en el diccionario no existe esa clave devuelve un error.
nombre_usuario = usuario['nombre']
print(f'Esta es el valor asociado a la clave "nombre": {nombre_usuario}')
#Si quiero acceder a un valor contenido en un diccionario anidado entonces puedo usar el metodo get() de la siguiente forma:
habilidades_usuario = usuario['habilidades'].get('base de datos')
print(f'El usuario posee habilidades de Base de datos": {habilidades_usuario}')

#Otra manera de acceder al valor de una clave es con el metodo get()
#d.get(clave, valor) devuelve el valor del diccionario d asociado a la clave clave. 
# Si en el diccionario no existe esa clave devuelve valor, y si no se especifica un valor por defecto devuelve None.
curso_usuario = usuario.get('curso')
print(f'Esta es el valor asociado a la clave "curso": {curso_usuario}')
#En el caso que no exista la llave puedo colocar un segundo parametro que muestre un valor por default en caso que la clave no exista
apellido_usuario = usuario.get('apellido', 'La llave ingresada no existe')
print(f'Esta es el valor asociado a la clave "apellido":{apellido_usuario}')

#Para agregar un valor al diccionario puedo hacerlo indicando el valor y haciendo referencia a la clave.
usuario = {
    'nombre': 'Pedro Gonzalez',
    'edad': 25,
    'curso': 'Programacion Web',
    'habilidades':{
        'programacion':'no',
        'base de datos':'si'
    },
    'nivel':'basico'
}
usuario['curso'] = 'Base de datos' # Actualiza el valor porque en este caso ya existe la clave
print(f'Datos del usuario:{usuario}')
usuario['telefono'] = 3624123456 # Agrega la clave y el valor porque no existen
print(f'Datos del usuario:{usuario}')

#Para eliminar el elemento puedo utilizar la sentencia 'del'
del usuario['edad']
print(f'Datos del usuario:{usuario}')

# Palabras reservadas in y not in en diccionarios -------------------------------------------------------
# Devuelve True si la clave especificada pertenece al diccionario y False en caso contrario.
usuario = {
    'nombre': 'Pedro Gonzalez',
    'edad': 25,
    'curso': 'Programacion Web',
    'habilidades':{
        'programacion':'no',
        'base de datos':'si'
    },
    'nivel':'basico'
}
existe = 'habilidades' in usuario
print(f'La clave "habilidades" se encuentra en el diccionario "usuario": {existe}')
no_existe = 'habilidades' not in usuario
print(f'La clave "habilidades" se encuentra en el diccionario "usuario": {no_existe}')
#--------------------------------------------------------------------------------------------------------

# Algunos metodos importantes para uso de diccionarios ----------------------------------------------------------------
#keys() : me permite obtener todas las llaves de un diccionario
usuario_keys = usuario.keys()
print(f'Estas son las claves que contiene el diccionario de "usuarios": {usuario_keys}')

#values() : me permite obtener todos los valores de un diccionario
usuario_values = usuario.values()
print(f'Estas son los valores que contiene el diccionario de "usuarios": {usuario_values}')

#items() : nos permite conocer las llaves con su correspondiente valor, separados en tuplas
usuario_items = usuario.items()
print(f'Estas son las claves y valores que contiene el diccionario de "usuarios": {usuario_items}')

#setdefault() - Muestra el valor que posee una clave y si no existe la agrega al diccionario
persona = {'name': 'Phill', 'edad': 22}

edad = persona.setdefault('edad')
print('Persona = ',persona)
print('Edad = ',edad)

#Si la clave no existe la agrega, por ejemplo
salario = persona.setdefault('salario')
print('Persona = ',persona)
print('Salario = ',salario) # Como no indico valor entonces asigna None por default
#Puedo indicar un valor por default en caso que no exista
salario = persona.setdefault('salario', 15000)
print('Salario = ',salario)


#fromkeys() - Crea un nuevo diccionario a partir de la secuencia de elementos dada con un valor proporcionado por el usuario.
llaves = ('a', 'e', 'i', 'o', 'u' ) #Puedo pasarle como parametro un diccionario, una tupla o una lista de valores

vocales = dict.fromkeys(llaves)
print('Este es el diccionario de vocales', vocales) #Como no indico los valores asociados a cada llave asigna valor None a cada llave

#Si quiero indicar valores a cada llave entonces escribo:
llaves = ('manzana', 'banana', 'pera', 'uvas', 'kiwi' )
valores = 100 #Asigna a todas las llaves el mismo valor

precios_frutas = dict.fromkeys(llaves, valores)
print('Este es el diccionario de precios de frutas:', precios_frutas)

#update() - agrega elementos al diccionario si la clave no está en el diccionario. 
# Si la clave está en el diccionario, la actualiza con el nuevo valor.
coordenadas = {
    'x': 3
}
#Puedo pasarle una tupla como parametro
coordenadas.update(y = 3, z = 0)
print(f'Este es el detalle de coordenadas: {coordenadas}')


#pop() - Elimina el valor asociado a una clave del diccionario. Si la clave no está devuelve el valor alternativo
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
eliminar_venta = ventas.pop('manzanas')
print('El elemento eliminado es:', eliminar_venta)
print('Los datos de ventas son:', ventas)
eliminar_venta = ventas.pop('uvas', 'No se ha encontrado el elemento') #Puedo indicar un segundo parametro en caso que no exista la clave
print('El elemento eliminado es:', eliminar_venta)

#popitem() - Elimina del diccionario la tupla formada por la ultima clave y valor del diccionario.
# Este metodo no recibe parametros
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
eliminar_venta = ventas.popitem()
print('El elemento eliminado es:', eliminar_venta)
print('Los datos de ventas son:', ventas)

#clear() - Elimina todos los pares del diccionario de manera que se queda vacío.
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
ventas.clear()
print('Los datos de ventas son:', ventas)

#copy() - Realiza una copia de un diccionario. Este metodo no recibe parametros
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
ventas_copia=ventas.copy()
print('Los datos de ventas son:', ventas)
ventas_copia.update(uvas=50, kiwi = 10)
print('Los datos de copia de ventas son:', ventas_copia)

# Algunas funciones importantes para uso de Tuplas ----------------------------------------------------

#len() - Me permite saber la longitud de un diccionario, es decir, la cantidad de elementos que contiene
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
print('La longitud del diccionario de ventas es:', len(ventas))

#max() - Devuelve la máxima clave del diccionario, siempre que las claves sean comparables.
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
print('La venta maxima del diccionario de ventas es:', max(ventas))

#min() - Devuelve la mínima clave del diccionario, siempre que las claves sean comparables.
ventas = { 
    'manzanas': 2, 
    'naranjas': 3, 
    'peras': 4 
}
print('La venta maxima del diccionario de ventas es:', min(ventas))

#sum() - Devuelve la suma de las claves del diccionario, siempre que las claves se puedan sumar.
ventas = { 
    25000: 'Enero' , 
    10000: 'Febrero', 
    40000: 'Marzo'  
}
print('La suma de ventas del diccionario de ventas es:', sum(ventas))

#Dictionary Comprehension ------------------------------------------------------------------------
#Es una forma elegante y concisa de crear un nuevo diccionario a partir de un iterable en Python.
#Consiste en un par de expresiones (key: value) seguido de una declaración for dentro de llaves {}.
#Por ejemplo si queremos hacer un diccionario con cada elemento como un par de un número y su cuadrado.

# Dictionary Comprehension
cuadrados = {
    x: x*x 
    for x in range(6)
}

print('Este es un diccionario en el que las llaves son numeros y los valores el cuadrado de las llaves \n', cuadrados)

#El codigo de arriba es equivalente a: 
cuadrados = {}
for x in range(6):
    cuadrados[x] = x*x
print('Este es un diccionario en el que las llaves son numeros y los valores el cuadrado de las llaves \n', cuadrados)

#Otro ejemplo: 
#Crear un diccionario en el que las llaves sean numeros impares y los valores el cuadrado de las llaves
# Dictionary Comprehension with if conditional
cuadrados_impares = {
    x: x*x 
    for x in range(11) 
        if x % 2 == 1
}

print('Este es un diccionario en el que las llaves son numeros impares y los valores el cuadrado de las llaves \n',cuadrados_impares)