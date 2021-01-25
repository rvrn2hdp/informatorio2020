'''Ejercicio 13: Contraseña aleatoria 
 Escriba una función que genere una contraseña aleatoria. 
 La contraseña debe tener una longitud aleatoria de entre 7 y 10 caracteres.
 Cada carácter debe seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII.
 Su función no tomará ningún parámetro y devolverá la contraseña
 generada aleatoriamente como su único resultado.
 Desarrolle un programa principal y muestre la contraseña generada aleatoriamente.
 Sugerencia: Probablemente encuentre útil la función chr cuando complete este ejercicio.
'''
from random import choice
import string

def random_char(y):
       return ''.join(choice(string.ascii_letters) for x in range(y))

def principal():
    print("Contraseña generada: ")
    print(random_char(10))
    
principal()