'''Ejercicio 6: Centrar una cadena en la terminal
 Escriba una función que tome una cadena de caracteres como primer parámetro
 y el ancho de la terminal en caracteres como segundo parámetro.
 Su función debe devolver una nueva cadena que consta de la cadena original
 y el número correcto de espacios iniciales para que la cadena original
 aparezca centrada dentro del ancho proporcionado cuando se imprima.
 No agregue ningún carácter al final de la cadena.
 Incluya un programa principal que use su función.'''

def centrar_cadena(cadena, ancho):
    return cadena.center(ancho, ' ')

def funcion_principal():
    miCadena = input("Ingrese una cadena: ")
    print(centrar_cadena(miCadena, 79))
    
funcion_principal()
