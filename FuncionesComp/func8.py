'''Ejercicio 8: Capitalízalo
 Muchas personas no usan letras mayúsculas correctamente,
 especialmente cuando escriben en dispositivos pequeños como teléfonos inteligentes.
 En este ejercicio, escribirá una función que
 capitaliza los caracteres apropiados en una cadena.
 Una "i" minúscula debe reemplazarse por una "I"
 mayúscula si está precedida y seguida de un espacio.
 El primer carácter de la cadena también debe estar en mayúscula,
 así como el primer carácter no espacial después de un ".", "!" o "?" Por ejemplo,
 si la función se proporciona con la cadena
 "¿a qué hora tengo que estar allí? ¿cuál es la dirección?"
 entonces debería devolver la cadena
 "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?".
 Incluya un programa principal que lea una cadena del usuario,
 la capitalice utilizando su función y muestre el resultado.
'''

def puntos(line):
    sentences = line.split(". ")
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = ". ".join(sentences2)
    return string2

def i_abierta(line):
    sentences = line.split("¿")
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = "¿".join(sentences2)
    return string2

def i_cerrada(line):
    sentences = line.split("? ")
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = "? ".join(sentences2)
    return string2

def capitalizar(cadena):
    cadena = puntos(cadena)
    cadena = i_abierta(cadena)
    cadena = i_cerrada(cadena)
    return cadena

def principal():
    print("\nFunción principal que lee y corrige una cadena de texto\n")
    micadena = input("ingrese una cadena de texto:\n")
    print(f"Cadena de texto antes de corregir:\n{micadena}")
    print(f"Cadena después de corregir:\n{capitalizar(micadena)}")

principal()
