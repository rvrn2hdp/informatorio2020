"""
a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa
 debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya 
 ingresado correctamente.

b) Modificar el programa anterior para que solamente permita 
 una cantidad fija de intentos. 
"""

def menu ():
    """
    docstring
    """
    print("\ncorrecto!\nbye!\n")

def checking_account(user, password):
    user_db = 3232
    password_db = 2322
    if user == user_db and password == password_db:
        return True
    else:
        return False

def login():
    intentos = 3
    while intentos >= 1:
        user = int(input("Ingrese su usuario: "))
        password = int(input("Ingrese su contraseña: "))

        if checking_account(user, password)==True:
            menu()
            break
        else:
            intentos -= 1
            print("datos ingresados incorrectos")
            print("Le quedan", intentos, "intentos\n")

print("\nprograma que simula el proceso de login\n")
login()