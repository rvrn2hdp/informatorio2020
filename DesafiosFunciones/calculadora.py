print("\nPrograma que simula ser una calculadora:\n")

def ingreso():
    ''' esta funcion lee un dato y lo transforma en entero
        utilizando try except para evitar errores de tipo'''
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue
        break
    return numero

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def producto(num1, num2):
    return num1*num2

def division(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1/num2

def operaciones(opc, n1, n2):
    ''' Esta funcion imprime la operacion elegida con los datos recibidos '''
    if opc == 1:
        print(n1, "+", n2, "=", suma(n1, n2))
    elif opc == 2:
        print(n1, "-", n2, "=", resta(n1, n2))
    elif opc == 3:
        print(n1, "x", n2, "=", producto(n1, n2))
    elif opc == 4:
        if n2 == 0:
            print("no se puede dividir por 0.")
        else:
            print(n1, "/", n2, "=", division(n1, n2))
    else:
        print("dato ingresado incorrecto.\n")

def menu():
    ''' Esta funcion muestra y lee la opcion que quiere el usuario
        ademas guardará los datos a procesar'''
    opcion = 1
    while opcion != 0:
        print("\nmenu de operaciones:")
        print("1 - Sumar")
        print("2 - Restar")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Salir\n")
        
        opcion = ingreso()
        if opcion != 0:
            print("\nIngrese los datos a procesar: ")
            dato1 = ingreso()
            dato2 = ingreso()
    
            operaciones(opcion, dato1, dato2)

def main():
    ''' funcion principal, afirma que el programa inicia e informa si termina. '''
    print("Inicio de programa")
    menu()
    print("\nprograma terminado")

main()
