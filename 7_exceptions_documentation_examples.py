'''
# Errores
# Los errores detienen la ejecución del programa y tienen varias causas. 
# Para poder estudiarlos mejor vamos a provocar algunos intencionadamente.
#---------------------------------------------------------------------------

# SyntaxError - Errores de sintaxis
# Por ejemplo:
print("Hola Mundo!"

# Resultado: SyntaxError: unexpected EOF while parsing
#-----------------------------------------------------------------------------

# NameError- Errores de nombre
# Por ejemplo: 
pint("Hola Mundo!")

# Resultado: NameError: name 'pint' is not defined
#-----------------------------------------------------------------------------

# Errores semánticos
# Estos errores son muy difíciles de identificar porque van ligados al sentido del funcionamiento y dependen de la situación. 
# Algunas veces pueden ocurrir y otras no.
# La mejor forma de prevenirlos es programando mucho y aprendiendo de tus propios fallos.


# pop() con lista vacía
# Por ejemplo: 
lista = []
lista.pop()

# Resultado: NIndexError: pop from empty list
#-----------------------------------------------------------------------------

# Intentar acceder a una posición de lista que no existe
# Por ejemplo: 

lista = [0,1,2,3,4,5]
print(lista[15])

# Resultado: IndexError: list index out of range
#-----------------------------------------------------------------------------

# Lectura de un string y operación sin conversión a número
# Por ejemplo: 

one = input("Introduce un número: ")
two = 5
print(f"{one}/{two} = {one/two}")

# Resultado: TypeError: unsupported operand type(s) for /: 'str' and 'int'
#-----------------------------------------------------------------------------

# Introducir una cadena que no es un número y tratar de hacer operaciones numéricas
# Por ejemplo: 

one = float(input("Introduce un número: "))
two = 4
print(f"{one}/{two} = {one/two}")

# Resultado: ValueError: could not convert string to float: 'aaa'
#-----------------------------------------------------------------------------

# División por cero
one = float(input("Introduce un número: "))
two = 0
print(f"{one}/{two} = {one/two}")

# Resultado: ZeroDivisionError: float division by zero
#---------------------------------------------------------------------------------------------------------------------------------


# Excepciones
# Las excepciones son bloques de código que nos permiten continuar con la ejecución de un programa pese a que ocurra un error. 
#----------------------------------------------------------------------------------------------------------------------------------

# Bloque try - except:
# Permite controlar situaciones excepcionales que generalmente darían error y en su lugar mostrar un mensaje o ejecutar una pieza de código alternativo.
# Por ejemplo: 

try:
    one = float(input("Introduce un número: "))
    two = 2
    print(f"{one}/{two} = {one/two}")
except:
    print("Ha ocurrido un error, introduce bien el número")

# Si introducimos un string nos mostrará el mensaje de la línea 76 en lugar de mostrar un error.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bloque try - except combinado con un ciclo while:
# En este caso debemos recordar colocar break antes de finalizar el bloque try para que no entre en un bucle infinito
# Retomemos el ejemplo anterior: 

while(True):
    try:
        one = float(input("Introduce un número: "))
        two = 2
        print(f"{one}/{two} = {one/two}")
        break
    except:
        print("Ha ocurrido un error, introduce bien el número")

# En este caso forzamos al usuario a introducir un número haciendo uso de un bucle while
# Repetimos la lectura por teclado hasta que lo haga bien y entonces romper el bucle con un break


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bloque try - except - else combinado con un ciclo while:
# Se utiliza para comprobar el caso en que todo funcione correctamente (no se ejecuta la excepción).
# Retomemos el ejemplo anterior:

while(True):
    try:
        one = float(input("Introduce un número: "))
        two = 2
        if one < 0:
            one = float(input("Introduce un número: "))
        else:
            print(f"{one}/{two} = {one/two}")
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break   # Importante romper la iteración si todo ha salido bien


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bloque try - except - finally combinado con un ciclo while:
# El bloque finally se ejecuta al final del código, ocurra o no ocurra un error
# Retomemos el ejemplo anterior:

while(True):
    try:
        one = float(input("Introduce un número: "))
        two = 2
        print(f"{one}/{two} = {one/two}")
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Excepciones múltiples:
# En una mismo programa pueden ocurrir muchos errores distintos y podemos tratar de forma diferente en cada caso.
# En esos casos esas lo que podemos hacer es asignar una excepción a una variable.

# Por ejemplo: 

try:
    one = input("Introduce un número: ")  # no transformamos a número
    print(5/one)
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__)
    print(type(e))


# Resultado: Ha ocurrido un error =>  TypeError

# Cada error tiene un identificador único que curiosamente se corresponde con su tipo de dato.
# Podemos mostrar la clase del error utilizando la sintaxis: print(type(e))
# Si retomamos el ejemplo anterior: 

try:
    one = input("Introduce un número: ")  # no transformamos a número
    print(5/one)
except Exception as e:  # guardamos la excepción como una variable e
    print(type(e))      # Imprimimos el tipo de error pero ademas nos indica que es una clase

# Resultado: <class 'TypeError'>
'''
# Entonces utilizamos los identificadores de tipo de error para poder actuar de acuerdo a cada tipo
# Si retomamos el ejemplo anterior: 
while True:
    try:
        one = float(input("Introduce un número divisor: "))
        print(5/one)
    except TypeError:
        print("No se puede dividir el número entre una cadena")
    except ValueError:
        print("Debes introducir una cadena que sea un número")
    except ZeroDivisionError:
        print("No se puede dividir por cero, prueba otro número")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__ )
    else:
        break
    finally:
        break

'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Invocación de excepciones:
# Podemos llamar a un error manualmente utilizando la palabra reservada 'is' en lugar de imprimirlo por consola

# Por ejemplo: 

def una_funcion(valor=None):
    if valor is None:
        print("Error! No se permite un valor nulo (con un print)")

una_funcion()

#-----------------------------------------------------------------------------------------------------------------4
# raise()
# La instrucción raise() para forzar a que ocurra una excepción específica.
# Por ejemplo: 

raise NameError('Hola')

# Resultado: NameError: Hola

# El único argumento a que le pasamos a raise() indica la excepción a generarse. 
# Veamos otro ejemplo, donde manejamos la excepción generada: 

def one_funcion(value=None):
    try:
        if value is None:
            raise ValueError("Error! No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")

one_funcion()

# En este caso lanzamos manualmente ValueError como resultado y tratamos la excepción usando el bloque except

#-----------------------------------------------------------------------------------------------------------------4
# assert
# Se utiliza para se fijar condiciones que debe cumplir un objeto y si éstas no se cumplen en un momento determinado, 
# producirá una excepción que hay que interceptar y tratar convenientemente.

# En el ejemplo a continuación se define una lista con seis elementos. 
# A continuación, mediante un bucle se irán eliminando elementos, uno a uno, desde el final de la lista. 
# La condición establecida para que no se produzca la excepción es que la lista tenga al menos dos elementos. 
# Cuando haya dos y se intente borrar de nuevo se producirá la excepción 'AssertionError'.
'''
try:  # bloque de código a vigilar
    lista = [1, 2, 3, 4, 5, 6]  # define lista
    print(lista)  # muestra lista
    while True:  # bucle infinito hasta error
        print('Elemento a borrar',lista[-1])
        lista.pop()  # borra elemento
        assert len(lista) > 1  # la lista debe tener al menos 2 
        print(lista)  # muestra lista después de borrado

except AssertionError:  # excepción para assert, se lanza cuando se intenta eliminar y quedan solo 2 elementos
    print('Error al intentar borrar elemento  ')  # mensaje de assert
    print('La lista debe contener al menos 2')
