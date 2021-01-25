"""Solicite al usuario el ingreso de 3 números,
e imprímalos de mayor a menor."""

def verificar_entero():
    while True:
        try:
            numero = int(input("Escribe un numero: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if numero < 0:
            print("Debes escribir un número positivo.")
            continue
        else:
            break
    
    return numero

def principal():
    print("\nprograma que muestra el numero mayor de tres numeros ingresados\n")
    num1 = verificar_entero()
    num2 = verificar_entero()
    num3 = verificar_entero()
    mayor = 0

    if num1 > num2 and num1 > num3:
        print(num1, "es el mayor.")
    elif num2 > num1 and num2 > num3:
        print(num2, "es el mayor.")
    elif num3 > num1 and num3 > num2:
        print(num3, "es el mayor.")
    elif num1 == num2 and num1 == num3:
        print("los números son iguales.")
    
principal()