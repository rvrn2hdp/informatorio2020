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

