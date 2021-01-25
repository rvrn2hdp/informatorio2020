'''Ejercicio 4: Mediana de tres valores
 Escriba una función que tome tres números como parámetros
 y devuelva el valor medio de esos parámetros como resultado.
 Incluya un programa principal que lea tres valores del usuario y muestre su mediana.'''

def medio(n1, n2, n3):
    if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
        return n1
    elif (n2 > n1 and n2 < n3) or ( n2 < n1 and n2 > n3):
        return n2
    elif (n3 > n1 and n3 < n2) or (n3 < n1 and n3 > n2):
        return n3
    else:
        return 0

def main():
    print("\nPrograma que calcula el valor medio de tres números:\n")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    
    print("El valor medio es:", medio(num1, num2, num3))

main()
