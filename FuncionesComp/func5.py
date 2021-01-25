''' Ejercicio 5: De número entero a número ordinal
 Las palabras como primero, segundo y tercero se refieren a números ordinales.
 En este ejercicio, escribirá una función que toma un número entero como su único parámetro
 y devuelve una cadena que contiene el número ordinal apropiado como único resultado.
 Su función debe manejar los enteros entre 1 y 12 (inclusive).
 Debería devolver una cadena vacía si se proporciona un valor fuera de este rango como parámetro.
 Incluya un programa principal que utilice su función mostrando
 cada número entero del 1 al 12 y su número ordinal.'''

def numero_cardinal(n):
    if n == 1:
        return 'Primero'
    elif n == 2:
        return 'Segundo'
    elif n == 3:
        return 'Tercero'
    elif n == 4:
        return 'Cuarto'
    elif n == 5:
        return 'Quinto'
    elif n == 6:
        return 'Sexto'
    elif n == 7:
        return 'Septimo'
    elif n == 8:
        return 'Octavo'
    elif n == 9:
        return 'Noveno'
    elif n == 10:
        return 'Decimo'
    elif n == 11:
        return 'Onceavo'
    elif n == 12:
        return 'Doceavo'
    else:
        return ''

def funcion_principal():
    num = int(input("Ingrese el numero cardinal: "))
    print(f"{num} es {numero_cardinal(num)}")
    
funcion_principal()