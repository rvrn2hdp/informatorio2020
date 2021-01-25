'''
Son el primer paso para entender la programación orientada a objetos en Python
Una función se encarga de contener el código necesario para realizar una tarea especifica. 
Una vez definida una función la vamos a poder utilizar todas las veces que sean necesarias.
'''

# Creacion de Funciones ---------------------------------------------------------------------------------------------------------------------------
# En la creacion de funciones hay dos conceptos importantes:
# La DEFINICION de la funcion y la LLAMADA a la funcion luego de definirla

# Para DEFINIR una funcion usamos la palabra def y definiremos el nombre de la función en minúsculas o usando guion bajo si incluye mas de una palabra
# Escribimos de la siguiente forma:

def saludar():
    '''Esta función imprime por consola el mensaje: Hola Mundo!'''
    print('Hola Mundo!')

# Luego de definir la funcion debemos hacer la LLAMADA para ejecutar la funcion que definimos arriba.
# Para llamar la funcion colocaremos el nombre de la funcion y luego parentesis.
saludar()

# Comunmente las funciones toman datos de entrada y retornan un resultado. 
# Una función puede no recibir ningún valor como parámetro y aun asi devolver algo como en el ejemplo de arriba.
# A los datos de entrada se los conoce como parámetros cuando definimos la funcion y se los indica con el nombre de variable.
# Para que la función pueda retornar un valor usaremos la palabra reservada return y el nombre de la variable que queremos devolver.
# Luego al llamar a la función debemos incluir entre los paréntesis el nombre de la variable que pasamos como parámetro sino obtendremos un error.

#Por ejemplo si definimos una funcion que sume dos numeros
def suma(numero1,numero2):                                                      #En este caso numero1 y numero2 son parametros
    '''Esta función realiza la suma dos números'''
    result_suma = numero1 + numero2
    print (f"Este es el resultado de la suma: {result_suma} \n")

# Al hacer la llamada a la funcion ahí pasamos los numeros como argumentos
suma(10,20)                                                                     #En este caso numero1 y numero2 son argumentos

# Parametros y argumentos en una funcion -----------------------------------------------------------------------------------------

# Al definir una función los valores que se reciben se denominan parámetros, pero durante la llamada los valores que se envían se denominan argumentos.
# Cuando se envían argumentos a una función, estos se reciben por orden en los parámetros definidos. 
# La asociación de los parámetros y los valores pasados a la función se hace normalmente de izquierda a derecha.
# En el ejemplo anterior, la función sumar recibe el valor de la variable numero_1 y la suma con el valor que recibe en segundo lugar, numero_2. 
# En este caso se dice que son argumentos por posición.
# También es posible modificar el orden de los parámetros si indicamos el nombre del parámetro al que asociar el valor a la hora de llamar a la función:
# Por ejemplo: sumar(numero_2 = 2, numero_1=3)

# El número de valores que se pasan como parámetro al llamar a la función tiene que coincidir con el número de parámetros que la función acepta según la declaración de la función.
# Si al momento de llamar una función la cual tiene definidos unos parámetros no pasa los argumentos correctamente provocará una excepción TypeError.
def suma(numero1,numero2):                                                      
    '''Esta función realiza la suma dos números'''
    result_suma = numero1 + numero2
    print (f"Este es el resultado de la suma: {result_suma} \n")

# Al hacer la llamada a la funcion ahí pasamos los numeros como argumentos
# suma(10)                                                                    
# Al pasar un solo numero como argumento da un error TypeError                  

# Para solucionar la excepción TypeError ejecutada al momento de la llamada a una función sin argumentos, 
# Entonces se puede asignar unos valores por defecto nulos a los parámetros, de esa forma puede hacer una comprobación antes de ejecutar.
def resta(a=None, b=None):                           #Los valores despues del signo = son los que definimos por defecto
    """Esta función imprime la resta de los dos valores pasados como
    parámetros"""
    if a ==None or b ==None:
        print("Error, debes enviar dos números a la función")
        return
    return a - b

resta(30, 10)
resta()

# Cuando definimos valores por default hay ciertas reglas que debemos seguir:
#   •	No se puede asignar un valor con espacios antes y despues del igual (num2 = None)
#   •	La asignación de los valores debe comenzar de deracha a izquierda y no deben haber saltos de linea


# A menudo no sabemos cuantos parámetros puede recibir una función, en estos casos usaremos un asterisco.
# En el caso de la funcion suma que usamos arriba sabíamos que recibiamos dos numeros como parametros.
# Si no sabemos cuantos numeros hay que sumar entonces usamos * y la palabra reservada args para indicar los valores de parametros que recibe

def suma(*args):
    """Esta función muestra como resultado la suma de valores pasados como
    parámetros"""
    total = 0
    for valor in args:
        total+=valor
    return total                                
result_suma = suma(10,50,25,60,80,5,90)
print(result_suma)

# Cuando usamos el * dentro de la función con un parámetro, el * agrupa todos los argumentos dentro de una tupla, esta tupla será asignada al parámetro
# El uso de * no nos limita a usar otros parámetros, pero tenemos que agregarlo siempre en el ultimo parámetro
# Siempre que usamos el * en una función debe tener el nombre args por estándar
# Otra forma de colocar un numero indeterminado de argumentos es usando el **, por convención el nombre del parámetro es kwargs
# Las claves de este diccionario serían los nombres de los parámetros indicados al llamar a la función y los valores del diccionario, los valores asociados a estos parámetros
def indeterminados(**kwargs):
    """Esta función imprime los valores pasados como parámetro"""
    print(kwargs)
indeterminados(n=5, c="Hola", l=[1, 2, 3, 4, 5])

# El uso de ** agrupa los elementos en un diccionario donde el nombre de la llave es el nombre del parámetro.
# Podemos utilizar args y kwargs como parametros de una misma funcion, pero debemos utilizarlos en ese orden
def super_funcion(*args, **kwargs):
    """Esta función imprime los valores pasados como parámetro por
    posición y nombre"""
    total = 0
    for arg in args:
        total += arg
    print("Total", "=>", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])
super_funcion(50, -1, 1.56, 10, 20, 300, c="Hola", n=3)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# Formas de terminar una funcion ------------------------------------------------------------------------------------------------------------------------
# Si no indicamos el valor a retornar la función(no escribimos return) nos devuelve None por defecto. None representa a un valor vacio
def una_funcion():
    """Esta función muestra por consola dos mensajes."""
    print("Este es un mensaje")
    print("Este es otro mensaje")

resultado = una_funcion()
print(resultado)

#Si retornamos un valor fijo llamando return
def una_funcion():
    '''Esta función muestra por consola dos mensajes.'''
    print("Este es un mensaje")
    print("Este es otro mensaje")

    return 2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Paso de argumentos por referencia y por valor ---------------------------------------------------------------------------------------------------------
# En Python al pasar una variable como argumento de una función estas se pasan por referencia o por valor.

# Paso por referencia: a lo que se pasa como argumento es una referencia o puntero a la variable. 
# La dirección de memoria en la que se encuentra el contenido de la variable, y no el contenido en sí. 
# Los valores mutables se comportan como paso por referencia ya que conservan los cambios hechos dentro de una funcion.

# Paso por valor : lo que se pasa como argumento es el valor que contenía la variable. 
# Los valores inmutables se comportan como paso por valor ya que conservan su valor original.

# La diferencia entre ambos es que en el paso por valor los cambios que se hagan sobre el parámetro no se ven fuera de la función, dado que los argumentos de la
# función son variables locales a la función que contienen los valores indicados por las variables que se pasaron como argumento. Es decir, en realidad lo que se 
# le pasa a la función son copias de los valores y no las variables en sí.
# Si quisiéramos modificar el valor de uno de los argumentos y que estos cambios se reflejarán fuera de la función tendríamos que pasar el parámetro por referencia.

def una_funcion_valor (nro):
    """Esta función actualiza los valores de los argumentos pasados
    como parámetro"""
    nro = nro + 3
    print(f"Este es el valor del numero una vez ejecutada la funcion: {nro}")

nro = 22
una_funcion_valor(nro)
print(f"Este es el valor del numero al llamarlo fuera de la funcion una vez ejecutada: {nro}")



#Al trabajar con valores inmutables se comportan como paso por valor ya que conservan su valor original sin importar los cambios y asignaciones que se hagan dentro de la funcion.

def una_funcion_referencia (lista):
    """Esta función actualiza los valores de los argumentos pasados
    como parámetro"""
    lista.append(3500)
    print(f"Este es el contenido de la lista una vez ejecutada la funcion: {lista}")

lista = [50,80,100]
una_funcion_referencia(lista)
print(f"Este es el contenido de la lista al llamarla fuera de la funcion una vez ejecutada: {lista}")




# Al trabajar con valores mutables se comportan como paso por referencia ya que conservan los cambios hechos dentro de la funcion.
# Si vemos el ejemplo tendremos el mismo valor dentro y fuera de la funcion ya que mantiene los cambios realizados al ejecutar la funcion.


# Variables Locales y Globales
# Todas las asignaciones de variables en la función almacenan el valor en la tabla de símbolos local
# Si declaramos las variables fuera de la función son variables globales, las  variables globales pueden ser utilizadas en mas de una función. 

animal = "León"                         # Es una variable GLOBAL

def mostrar_animal():
    """Esta función muestra el valor de la variable animal por consola"""
    print(animal)

mostrar_animal()
print(animal)

# Si necesitamos modificar el valor de la función tendrá un valor dependiendo de donde se la llame ya que depende del contexto (namespace)
animal = "León"                         # Es una variable GLOBAL

def mostrar_animal():
    """Esta función muestra el valor de 
    la variable animal por consola"""
    animal = "Ballena"                  # Es una variable LOCAL
    print(animal)

mostrar_animal()
print(animal)

# Si probamos el ejemplo anterior veremos que el valor dentro y fuera de la funcion varía ya que depende del contexto
# Las variables locales mantienen su valor dentro de la ejecucion de la funcion
# Las variables globales mantienen su valor en mas de una funcion y depende del contexto que cambie su valor
# Si queremos modificar el valor de una variable global utilizaremos la palabra reservada “global”

animal = "León"                         

def mostrar_animal():
    """Esta función muestra el valor de 
    la variable animal por consola"""
    global animal 
    animal = "Ballena"                  
    print(animal)

mostrar_animal()
print(animal)

# Sentencia pass
# Es una sentencia 
# Es una declaración simple que se utiliza cuando en un bloque de código no se quiere hacer nada
# Se utiliza cuando se requiere por sintaxis una declaración pero no se quiere ejecutar ningún comando o código. 
# También se utiliza en lugares donde donde el código irá finalmente, pero no ha sido escrita todavía (utilizándolo como un relleno temporal, hasta que se escriba el código final).

# Primer ejemplo

for letra in "Python":
    if letra == "h":
        pass
    print ("Letra actual :" + letra)

# Segundo ejemplo
var = 10
while var > 0:
    var = var -1
    if var == 5:
        pass
    print ("Valor actual de la variable :" + str(var))

print ("fin del script")

# Diferencia entre continue y pass
# Continue termina la iteración actual, pero continua con el ciclo, volviendo al inicio del bucle en la siguiente iteración
# Pass no hace nada y pasa a la siguiente instrucción.

for x in (1, 2, 3):
    print (x)
    continue
    print (str(x) + " nuevamente")

#-----------------------------------------

for x in (1, 2, 3):
    print (x)
    pass
    print (str(x) + " nuevamente")


# En el primer ejemplo al llegar a la letra h no se ejecuta nada (se pasa), siguiendo con la ejecución de la siguiente linea (la linea 7). 
# Lo mismo ocurre con el 5 en el segundo ejemplo

# locals() y globals()
# Proporcionan acceso de tipo diccionario a las variables locales y globales.
'''
 La forma en que Python gestiona las variables se debe a los espacios de nombre (namespaces) donde se lleva un seguimiento de las variables. 
 Un espacio de nombres se puede tratar como un diccionario donde las keys son los nombres de las variables y las values son los valores de dichas variables.
'''
# Veamos un ejemplo de uso de locals():

# locals() a nivel global
# Python program to understand about locals 

# Mostremos que datos se muestran si imprimimos por consola locals()
print("This is using locals() : ", locals()) 

# Mostremos que datos se muestran si imprimimos por consola globals()
print("This is using globals() : ", globals()) 

# Veremos que en ambos casos nos devuelven la tabla de nombres de variables en formato de diccionario.

# Usando locals() a nivel local
# Probamos primero que nos muestra al no tener variables locales definidas
def demo1(): 
    ''' Esta funcion verifica si hay variables 
        definidas a nivel local usando locals()'''
    print("Aqui no hay variables locales definidas : ", locals())

# Probamos nuevamente que nos muestra al tener una variable local definida.
def demo2():
    ''' Esta funcion verifica si hay variables 
        definidas a nivel local usando locals()'''
    nombre = "Juan Pérez"
    print("Aqui hay variables locales definidas : ", locals()) 

# Llamamos ambas funciones para comparar que nos muestra en cada caso
demo1() 
demo2() 

# Ejemplo para mostrar que locals() es una función de solo lectura
# Utilizamos los ejemplos definidos arriba
def demo1(): 
    ''' Esta funcion verifica si hay variables 
        definidas a nivel local usando locals()'''
    print("Aqui no hay variables locales definidas : ", locals()) 

# Probamos nuevamente que nos muestra al tener una variable local definida.
def demo2(): 
    ''' Esta funcion verifica si hay variables 
        definidas a nivel local usando locals()'''
    nombre = "Juan Pérez"
    print("Aqui hay variables locales definidas : ", locals()) 
    print("Valor antes de actualizar nombre : ", nombre) 

    # Probamos de cambiar el valor de la variable nombre 
    locals()['nombre'] = "Juanito Smith"
    print("Valor despues de actualizar nombre : ", nombre) 

# Llamamos ambas funciones para comparar que nos muestra en cada caso
demo1() 
demo2() 
# Comprobamos que por mas que asignamos un valor distinto mantiene su valor original.

# Veamos ahora un ejemplo de uso de globals():
# Definimos una variable global
a = 5

def funcion_suma(): 
    ''' Esta funcion suma dos valores y 
        luego reasigna el valor usando globals()
    '''
    c = 10
    d = c + a 

    # Usamos globals() para redefinir el valor de 'a' que esta definida como una variable global
    globals()['a'] = d 
    print (a) 

# Llamamos a la funcion  
funcion_suma() 

#--------------------------------------------------------------------------------
# Otro ejemplo usando la funcion de arriba
nombre = 'Juan Pérez'
print('Valor antes de la modificación:', nombre) 

def demo2(): 
    ''' Usamos globals() para redefinir el valor de nombre''' 
    globals()['nombre'] = 'Juanito Smith'
    print('Valor después de la modificación:', nombre) 

# Llamamos a la funcion  
demo2() 

# Comprobamos que globals() permite modificar el valor de una variable global.
#--------------------------------------------------------------------------------
# Otro ejemplo del uso de globals() y locals() podemos verlo en el siguiente ejemplo:

def mensaje(nombre):
    """Esta función retorna un mensaje de saludo"""
    return "Hola " + nombre

# Utilizamos globals() para poder retornar una funcion especificada como global que pasamos como parámetro
def mensaje_personalizado(nombre, funcion=""):
    """Llamada de retorno a nivel global"""
    return globals()[funcion](nombre)

print(mensaje_personalizado("Maria", "mensaje"))
nombre_funcion = "mensaje"
# Utilizamos locals() para poder mostrar por consola una funcion especificada en una variable que pasamos como parámetro
print(locals()[nombre_funcion]("Pedro"))


'''La gran diferencia es que locals() no devuelve el verdadero espacio de nombres local, 
sino una copia (Así que cambiarlo no hace nada con los valores de las variables del espacio local); 
y en cambio globals() devuelve el verdadero espacio de nombres global, no una copia (Así que los cambios 
que haga en el diccionario devuelto por globals afectan directamente a las variables globales).'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funciones Lambda
'''
Las funciones lambda son conocidas como funciones anónimas, son expresadas en una línea de código ya que 
comúnmente realizan tareas pequeñas.
Defino lambda luego los parámetros y podemos darle un valor por default si tenemos mas de un parámetro 
los separamos por comas. No se usa return porque todas las funciones lamba retornan un valor.
Las funciones lambda son la base de la programación funcional en Python
'''
# Supongamos que tenemos una funcion que hace la conversion de temperatura en diferentes escalas
# Si definieramos una funcion para hacer esto escribiríamos:

def convertir_temperatura(grados):
    return grados * 1.8 + 32

# Podemos asignar una función a una variable:
funcion_variable = convertir_temperatura
# Utilizo la variable para llamar a la funcion:
resultado = funcion_variable(32)
print(resultado)

# Esta funcion definida arriba puede definirse como una función lambda:
''' Para definir una funcion lambda tengo que escribir la palabra lambda,
luego defino el/los parámetros que recibe y puedo asignar un valor por defecto, 
luego coloco : y a continuacion el detalle de acciones que realiza la función''' 
# En este caso mi funcion recibe como parámetro grados al que le asigno el valor por defecto 0
# Despues de colocar : coloco lo que debe retornar mi función
funcion_variable = lambda grados = 0 :  grados * 1.8 + 32

resultado = funcion_variable(32)
print(resultado)


# Estas son algunas formas en las cuales podemos crear funciones lambdas más complejas:

lambda_sin_parametros = lambda : True       # Esta funcion no recibe parametros y siempre retorna True

lambda_muchos_valores = lambda one, two=10, three=20 : one + two + three  # Esta funcion recibe 3 numeros como parametros y retorna la suma de ellos

lambda_asterisco = lambda *args: args[0] # Esta funcion tiene un numero indeterminado de parametros y devuelve el valor de la primera posicion

lambda_doble_asterisco = lambda **kwargs: kwargs[0] # Esta funcion tiene un numero indeterminado de parametros y devuelve el valor de la primera posicion

lambda_asteriscos_combinado = lambda *args, **kwargs: kwargs.get('key', False)


# Funcion map()
# La función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...)
# Nos retornara un objeto map que posteriormente podemos convertir a lista o tupla
# La sintaxis de la funcion map es la siguiente: map(funcion, objeto iterable) y devuelve un objeto como resultado.
# Mostremos primero el ejemplo usando map() con una funcion simple y luego haciendo lo mismo con funciones lambda
def cuadrado(numero):
    return numero*numero

lista = [1,2,3,4,5,6,7,8,9,0]
resultado = map(cuadrado, lista)    # Utilizo la funcion map() para iterar en la lista aplicando la funcion cuadrado
print(resultado)                    # Devuelve un objeto de tipo map
lista_resultado = list(resultado)   # Lo transformo a una lista
print(lista_resultado)


# Es posible usar map() junto con una funcion lambda: 

lista = [1,2,3,4,5,6,7,8,9,0]
# Puedo asignar la funcion lamba a una variable como arriba o pasarla directamente como argumento a map()
resultado = map(lambda numero: numero * numero, lista)
# Como map() devuelve un objeto de tipo map() entonces tengo que transformarlo a lista o tupla para ver su contenido.
lista_resultado = list(resultado)
print(lista_resultado)

# Funcion filter()
# Al igual que map() nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...)
# Crea una lista nueva a partir de los elementos para los cuales función devuelve 'True'
# La sintaxis de la función es: filter(funcion, iterable) y devuelve un objeto como resultado.

lista = [1,2,3,4,5,6,7,8,9,0]
# En este caso obligatoriamente tengo que definir una condición que va a ser el filtro de los elementos de la lista.
# La idea es que obtengamos como resultado una lista que contenga solo los números pares.
lista_pares = filter(lambda numero: numero % 2 == 0, lista)
# Como devuelve un objeto entonces tengo que transformarlo a lista o tupla para ver su contenido.
lista_res = list(lista_pares)
print(lista_pares)    
print(lista_res)    

# Funcion reduce()
# Se aplica siempre dos argumentos a los elementos en el iterable, de izquierda a derecha de forma acumulativa.
# La sintaxis de la función es: reduce(funcion, iterable) y devuelve un objeto como resultado.
# En Python 3 no esta incluida como función por lo que hay que importar el módulo 'functools' que la contiene
from functools import reduce 

lista = [1,2,3,4,5,6,7,8,9,0]
# Una vez definido el iterable, la función reduce() toma dos elementos de la lista y calcula el resultado
# En la seguna iteracion toma los siguientes dos elementos y los suma acumulando con el resultado obtenido en la primer iteración
lista_suma = reduce(lambda one, two: one+two , lista)
# En este caso obtenemos como resultado un numero que indica la suma de todos los elementos de la lista seleccionados de a pares.
print(lista_suma)    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funciones anidadas
''' 
    En Python las funciones se encuentran al mismo nivel que otros objetos de Python como enteros, cadenas, módulos, etc. 
    Se pueden crear y destruir de forma dinámica, pasar a otras funciones, devolver como valores, etc.
    Python admite el concepto de "función anidada" o "función interna", que es simplemente una función definida dentro de otra función.
'''
# Veamos un ejemplo simple de como definir una función anidada. 

def reproducir_playlist(playlist):
    def reproducir():
        for cancion in playlist:
            print(cancion)
    
    print(playlist)

playlist = ['Cancion 1', 'Cancion 2', 'Cancion 3', 'Cancion 4', 'Cancion 5']
reproducir_playlist(playlist)

# Si ejecuto el codigo de arriba puedo ver que se muestra la lista completa pasada como argumento pero no se ejecuta el print dentro del ciclo 'for'
# Al no realizar la llamada a la función interna entonces no se ejecuta nunca
# Por ello no debemos olvidar de realizar la llamada de la funcion interna ('reproducir()') dentro de la funcion externa ('reproducir_playlist()')

def reproducir_playlist(playlist):
    def reproducir():
        for cancion in playlist:
            print(cancion)
    # Agregamos la llamada a la función interna dentro de la función
    reproducir()                                 
    print(playlist)

playlist = ['Cancion 1', 'Cancion 2', 'Cancion 3', 'Cancion 4', 'Cancion 5']
# Agregamos la llamada a la función externa fuera de la función
reproducir_playlist(playlist)

# Si llamamos a la funcion interna fuera de la funcion reproducir_playlist() veremos que nos muestra un error que indica que reproducir() no esta definida
def reproducir_playlist(playlist):
    def reproducir():
        for cancion in playlist:
            print(cancion)                               
    print(playlist)

playlist = ['Cancion 1', 'Cancion 2', 'Cancion 3', 'Cancion 4', 'Cancion 5']
# Agregamos la llamada a la función interna fuera de la función
# reproducir()  
# Agregamos la llamada a la función externa fuera de la función
reproducir_playlist(playlist)

# Esto se debe al alcance de la función reproducir(), al estar definida dentro de la función hace que si la llamamos fuera no exista.
# Las funciones anidadas se crean con el objetivo de utilizar el alcance como protección de de todo lo que sucede fuera de la función.
# En ese caso, la función se ocultará del alcance global.
# Veamos otro ejemplo para ver el alcance de las variables y las operaciones que podemos hacer dentro de cada función:
def externa(one):
    ''' Esta funcion recibe como parametro 
        el primer numero para realizar la multiplicación
    '''  
    def interna(two):
        ''' Esta funcion recibe como parametro 
        el segundo numero para realizar la multiplicación
        y retorna el producto de ambos números
        '''  
        return one * two
    # Llamada de la función interna
    return interna

# Llamado de la función externa
resultado = externa(10)

print(resultado(5))

# El ejemplo realiza el producto entre dos numeros y muestra que una función interna es capaz de acceder a variables accesibles en la función externa.
# ¿Qué pasa si intentamos cambiar las variables de la función externa desde dentro de la función interna?

def externa(): 
    ''' Esta funcion no recibe parametros
        y retorna la suma de dos números
    '''  
    x = 2      # Defino una variable local dentro de la función externa
    def interna(a): 
        # Definamos una nueva variable local dentro de la función interna con el mismo nombre en lugar de cambiar el valor de x de la función externa
        x = 6
        print (a+x)
    print (x) # Mostramos el valor de x en la funcion externa
    interna(3)

externa()

# Comprobaremos que es posible para nosotros mostrar el valor de una variable definida dentro de la función externa desde la función interna, pero no cambiarla. 
# La linea 553 nos ayudó a crear una nueva variable x = 6 dentro de la función interna lugar de cambiar el valor de la variable x definida en la función externa.

# Veamos ahora el siguiente ejemplo: 
def externa(x):  
    ''' Esta funcion no recibe parametros
        y retorna el incremento de un número
    '''  
    # La funcion interna esta oculta de las funciones que podamos tener definidas fuera de la funcion externa()
    def interna(x):
        return x + 2
    y = interna(x)
    print(x, y)

# interna(5)  
externa(5)

# Al probar el ejemplo anterior obtendremos un error: NameError: name 'interna' is not defined
# Probemos ahora agregando la llamada a la funcion externa() y comentando la llamada a la funcion interna()
def externa(x):  
    ''' Esta funcion no recibe parametros
        y retorna el incremento de un número
    '''  
    # La funcion interna esta oculta de las funciones que podamos tener definidas fuera de la funcion externa()
    def interna(x):
        return x + 2
    y = interna(x)
    print(x, y)

#interna(5)  
externa(5)

# Con esta prueba comprobamos de que la función interna está protegida de lo que sucede fuera de ella
# Ya que la variable x dentro de la función interna no se ve afectada por el valor pasado como parámetro x de la función externa. 
# En otras palabras, las variables dentro de la función interna no son accesibles fuera de ella. 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Closures() 
# Se utiliza para que una función genere dinámicamente otra función y que esta nueva función pueda acceder a las variables locales aun cuando la función haya terminado
# Se utiliza para evitar el uso de variables globales y proporcionan alguna forma de ocultar datos. Se usan en conjunto con los decoradores que veremos mas adelante.
# Utilizan funciones anidadas para vincular o pasar datos a una función sin pasar necesariamente los datos a la función a través de parámetros.
# Un closure es causado por una función interna, pero no es la función interna. 
# El closure funciona cerrando la variable local en el momento de ejecucion, pero que se mantiene después de que la ejecucion de la función haya terminado de ejecutarse.

# Veamos un ejemplo:

def mostrar_mensaje(nombre):  
    ''' Esta función crea de forma dinámica 
        la función mostrar_nombre().
    '''
    def mostrar_nombre():
        print('Hola, mi nombre es ' + nombre)
    return mostrar_nombre                       # Retorno un objeto en lugar de llamar a la función

mostrar = mostrar_mensaje('Juanito González')  
mostrar()  

# En el ejemplo anterior la función mostrar_mensaje() crea y retorna una función, la función mostrar_nombre() es el closure.

'''
Condiciones que deben cumplirse para crear un cierre en Python:
- Debe haber una función anidada
- La función interna tiene que hacer referencia a un valor recibe la funcion externa (closure).
- La función closure tiene que devolver la función anidada.
'''

# Los closures() tienen memoria, siendo capaz de recordar, y utilizar, las variables lo locales y no locales definidas previamente:
def mostrar_mensaje2(nombre):  
    ''' Esta función crea de forma dinámica 
        la función mostrar_nombre().
    '''
    mensaje = 'Hola ' + nombre

    def mostrar_nombre():
        print(mensaje)

    return mostrar_nombre

mostrar2 = mostrar_mensaje2('Juanito González')  
mostrar2()  

# Vemos que aunque la función mostrar_mensaje ha dejado de ejecutarse, y con ello su alcance tambien termina, 
# pero es posible seguir accediendo a las variables definidas dentro de ella. 

# Para que los closures funcionen con variables inmutables como números y cadenas, tenemos que usar la palabra clave nonlocal.
# Las variables locales no se pueden modificar el funciones anidadas, si queremos modificar variables locales tambien usamos la palabra clave nonlocal.
# La palabra reservada nonlocal se usa solo cuando estamos trabajando con valores inmutables.

# Veamos un ejemplo aplicando la palabra reservada nonlocal:
def contar():
    ''' Esta función crea 
        una función de contador
    '''
    cont = 0
    def interna():

        nonlocal cont
        cont += 1
        return cont

    return interna


contador = contar()

resultado = contador()
print(resultado)

resultado = contador()
print(resultado)

resultado = contador()
print(resultado)

# Al probar esta función quitando la palabra reservada nonlocal de la línea 658 veremos que no permite que se actualice el valor de cont
# Nos mostrará este error si lo ejecutamos: UnboundLocalError: local variable 'cont' referenced before assignment
# Al utilizar nonlocal lo que permite es poder modificar el valor de la variable cont en cada ejecución

'''
Entonces, ¿cuando y para qué sirven los cierres?

- Los cierres pueden evitar el uso de valores globales y proporcionan alguna forma de ocultar datos. 
- También puede proporcionar una solución orientada a objetos para el problema (volvemos a verlo cuando veamos orientación a objetos).

- Cuando hay pocos métodos (un método en la mayoría de los casos) para implementar en una clase, los cierres pueden proporcionar 
una solución alternativa y más elegante. Pero cuando el número de atributos y métodos aumenta, es mejor implementar una clase
(volvemos a verlo cuando veamos orientación a objetos).

'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Decoradores
# Se utilizan para agregar funcionalidad a un código existente.
# Los decoradores hacen un uso extensivo de los closures.
# Un decorador no es más que una función la cual toma como entrada o parámetro una función y a su vez retorna otra función como resultado.
# Entonces al momento de implementar un decorador estaremos trabajando, con por lo menos, 3 funciones. 
'''
Condiciones que deben cumplirse para crear un decorador en Python:
- Debe haber una función que es la que funciona como decorador
- Debe existir una función a decorar que se recibe como un parámetro.
- La función decorada es la función que devuelve el decorador.

Con un decorador podemos cambiar el comportamiento de un función, método o clase
sin modificar su código, esa es la ventaja de utilizar un decorador. Se crea un
“envoltura” alrededor de la función a decorar donde se encuentra el código que
deseamos añadir, esta envoltura y la función original, es la nueva función que
obtenemos.

La sintaxis de una funcion decoradora es la siguiente: 
def decorador(funcion):
    def funcion_envoltura():
        print(“antes de la funcion”)
        funcion()
        print(“despues de la funcion”)
    return funcion_envoltura

Para utilizar la función decoradora utilizaremos el símbolo @ seguido del nombre de la función:
@decorador
def funcionPrueba():
    print(";no quiero que nadie modifique el codigo de la funcion")

Luego tenemos que ejecutar la funcion
funcionPrueba()

'''
# Veamos un ejemplo: 
# Primero vamos a plantear una funcion simple y luego vemos como la transformamos a un decorador

def agrega_numero_de_linea(texto):
    ''' Esta funcion toma un texto que consiste de varios renglones 
        y a cada uno de estos le agrega como prefijo el número de 
        línea que le corresponde.
    '''
    lineas = []
    for numero, linea in enumerate(texto.split('\n'), 1):
        lineas.append(f'{numero:6} {linea}')
    return '\n'.join(lineas)

def diccionario_a_texto(diccionario):
    ''' Esta funcion transforma un diccionario a 
        un formato de texto
    '''
    texto = ''
    for llave, valor in diccionario.items():
        texto += f'{llave:12}: {valor}\n'
    return texto
juan = {
    'nombre': 'Juan Pérez',
    'edad': 25
}
print(diccionario_a_texto(juan))

# Si quisieramos agregar los numeros de linea al diccionario de la función anterior deberíamos escribir:
print(agrega_numero_de_linea(diccionario_a_texto(juan)))

# ---------------------------------------------------------------------------------------------------- #
# Ahora planteemos las mismas funciones utilizando el concepto de decorador
# El decorador nos ayudará a ocultar el código que numera la línea y a aprovecharla en otras funciones de una manera fácil y elegante
# Nuestra función decoradora recibe como argumento otra definida en el exterior, y devuelve una tercera función que esta anidada. 
# La parte interesante es que la función anidada invoca a la externa y posteriormente procesa dicho resultado, agregando la funcionalidad del decorador al resultado final.

def con_linea_numerada(funcion):
    ''' Esta es una funcion decoradora
    '''
    def agrega_numero_de_linea(*args, **kwargs):
        ''' Esta funcion toma un texto que consiste de varios renglones 
            y a cada uno de estos le agrega como prefijo el número de 
            línea que le corresponde.
        '''
        resultado = funcion(*args, **kwargs)
        lineas = []
        for numero, linea in enumerate(str(resultado).split('\n'), 1):
            lineas.append(f'{numero:6} {linea}')
        return '\n'.join(lineas)
    return agrega_numero_de_linea

# Para utilizar el decorador colocamos @ para llamar a la funcion decoradora y luego el nombre. 
@con_linea_numerada

# A continuación definimos la funcion que vamos a decorar: 
def diccionario_a_texto2(diccionario):
    texto = ''
    for llave, valor in diccionario.items():
        texto += f'{llave:12}: {valor}\n'
    return texto

juan = {
    'nombre': 'Juan Pérez',
    'edad': 25
}
print(diccionario_a_texto2(juan))




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Generadores

'''
Es una función especial que produce secuencias completas de resultados en lugar de ofrecer un único valor. 
En apariencia es como una función típica pero en lugar de devolver los valores con 'return' lo hace con la 
declaración 'yield'(define tanto a la propia función como al resultado que produce).
Una característica importante de los generadores es que tanto las variables locales como el punto de inicio 
de la ejecución se guardan automáticamente entre las llamadas sucesivas que se hagan al generador, es decir, 
a diferencia de una función común, una nueva llamada a un generador no inicia la ejecución al principio de 
la función, sino que la reanuda inmediatamente después del punto donde se encuentre la última declaración 
yield (que es donde terminó la función en la última llamada).
'''
# Veamos un ejemplo:
def funcion_generadora():
    ''' Esta funcion genera una lista 
        de tres numeros pasados como strings
    '''
    yield "uno"   
    yield "dos"
    yield "tres"

for valor in funcion_generadora():
    print(valor)  # Imprimo el valor generado en cada iteración: uno, dos, tres

# Creo un objeto generador asignando la funcion a una variable
generador = funcion_generadora()
print(generador)  # generator object funcion_generadora at 0x7f75ffad55e8
# Muestro el tipo de objeto que devuelve la función
print(type(generador))  # class 'generator'

# Convierto a lista el objeto generador y muestra elementos
lista = list(generador)
print(lista)  # ['uno', 'dos', 'tres']
print(type(lista))  # class 'list'

# Las funciones generadoras siempre se utilizan en conjunto con un ciclo de iteración

# Veamos otro ejemplo simple de aplicación de generadores:
def tabla_multiplicar(numero, maximo=10):
    ''' Esta funcion genera el resultado 
        la tabla de multiplicar de un numero 
        pasado como parametro
    '''
    for posicion in range(1, maximo+1):
        yield numero*posicion

for resultado in tabla_multiplicar(9):
    print(resultado)                    # Muestra solo el resultado de cada multiplicacion


# Puedo mejorar el formato de salida de la tabla de multiplicar modificando la linea 683 del programa anterior:
def tabla_multiplicar2(numero, maximo=10):
    '''Esta funcion genera el resultado 
        la tabla de multiplicar de un numero 
        pasado como parametro
    '''
    for posicion in range(1, maximo+1):
        yield numero*posicion, numero, posicion

for resultado, numero, posicion in tabla_multiplicar2(9):
    print(numero, 'X', posicion, '=', resultado)    # Muestra la tabla formato: 2 x 2 = 4

# Veamos un ejemplo más complejo:
def generador_diez_nros(inicio):
    ''' Esta funcion genera 
        una sucesión de 10 valores numéricos 
        a partir de un valor inicial
    '''
    fin = inicio + 10    
    while inicio < fin:
        inicio+=1
        yield inicio, fin

for inicio, fin in generador_diez_nros(23):
    print(inicio, fin)

# Este ejemplo muestra como se almacenan los valores de las variables en cada ciclo y el punto donde se reanuda el bucle en cada llamada.
'''
En un generador la declaración yield puede aparecer en varías líneas e incluso dentro de un bucle. 
Como vimos en los ejemplos anteriores no es necesario usar la palabra return porque la función siempre retorna un objeto por defecto.
El intérprete Python producirá una excepción de tipo StopIteration si encuentra el comando return durante la ejecución de un generador.
'''