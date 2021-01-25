'''Ejercicio 11: ¿Es un número primo?
 Un número primo es un número entero mayor
 que 1 que solo es divisible por uno y por sí mismo.
 Escriba una función que determine si su parámetro es primo o no,
 devolviendo True si lo es y False en caso contrario.
 Escriba un programa principal que lea un número entero del usuario
 y muestre un mensaje que indique si es primo o no.
 Asegúrese de que el programa principal no se ejecutará
 si el archivo que contiene su solución se importa a otro programa.
'''

def primo(n):
    cont = 0
    if n >= -1 and n <= 1:
        return False
    elif n <= 2 or n >= 2:
        for i in range(1, n+1, 1):
            if n % i == 0:
                cont += 1
        if cont == 2:
            return True
        else:
            return False

def principal():
    print("Inicio")
    numero = int(input("Ingrese un numero: "))
    if primo(numero):
        print(numero, "es primo.")
    else:
        print(numero, "no es primo.")

principal()