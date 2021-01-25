"""Intenta desarrollar un programa que solicite la cantidad
de intentos fallidos de ingreso de una contraseña.
Si la cantidad es mayor a 5 veces, debes informar
“Cuenta Bloqueada”
Prueba y practica"""

intentos = 5 # se establece la cantidad de intentos
contrasenia = None # se crea la variable que guardará el valor que se comparará con la contraseña

while intentos >= 1:
    contrasenia = int(input("ingrese su contraseña:"))
    if contrasenia == 1234:
        print("contraseña correcta.")
        break
    else:
        print("contraseña incorrecta.")
        intentos -= 1
        print("le quedan", intentos, "intentos.")
