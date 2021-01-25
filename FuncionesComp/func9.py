'''Ejercicio 9: ¿Un string representan un entero?
 En este ejercicio escribirá una función llamada es_entero que determina
 si los caracteres en una cadena representan un número entero válido.
 Al determinar si un string representa un número entero, debe ignorar cualquier
 espacio en blanco inicial o final. Una vez que se ignora este espacio en blanco,
 una cadena representa un número entero si su longitud es al menos
 1 y solo contiene dígitos, o si su primer carácter es + o -
 y el primer carácter va seguido de uno o más caracteres,
 todos los cuales son dígitos
 Escriba un programa principal que lea una cadena del usuario
 e informe si representa o no un número entero.
 Sugerencia: Puede encontrar los métodos lstrip,
 rstrip y / o strip para cadenas útiles cuando complete este ejercicio.
'''

def es_entero(cadena):
    cadena =  cadena.strip(' ')
    print(cadena)
    if len(cadena) > 0 or (cadena[0] == '+' or cadena[0] == '-') and cadena[0:].isdigit():
        return "Es un número entero."
    else:
        return "No es un número entero."

def principal():
    micadena = input("Ingrese un numero: ")
    print(es_entero(micadena))

principal()