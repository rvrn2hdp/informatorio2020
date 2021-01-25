# Closures() 
# Se utiliza para que una función genere dinámicamente otra función y que esta nueva función
# pueda acceder a las variables locales aun cuando la función haya terminado
# Se utiliza para evitar el uso de variables globales y proporcionan alguna forma de ocultar datos.
# Se usan en conjunto con los decoradores que veremos mas adelante.
# Utilizan funciones anidadas para vincular o pasar datos a una función sin pasar necesariamente
# los datos a la función a través de parámetros.
# Un closure es causado por una función interna, pero no es la función interna. 
# El closure funciona cerrando la variable local en el momento de ejecucion, pero que se mantiene después
# de que la ejecucion de la función haya terminado de ejecutarse.

# Veamos un ejemplo:

def mostrar_mensaje(nombre):  
    ''' Esta función crea de forma dinámica 
        la función mostrar_nombre().
    '''
    def mostrar_nombre():
        print('Hola, mi nombre es ' + nombre)
    return mostrar_nombre # Retorno un objeto en lugar de llamar a la función

mostrar = mostrar_mensaje('Juanito González')  
mostrar()  

# En el ejemplo anterior la función mostrar_mensaje() crea y retorna una función,
# la función mostrar_nombre() es el closure.

'''
Condiciones que deben cumplirse para crear un cierre en Python:
- Debe haber una función anidada
- La función interna tiene que hacer referencia a un valor recibe la funcion externa (closure).
- La función closure tiene que devolver la función anidada.
'''