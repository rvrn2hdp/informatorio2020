'''Ejercicio 7 : ¿Es un triángulo válido?
 Si tiene 3 varillas, posiblemente de diferentes longitudes, puede o no ser posible
 colocarlas para que formen un triángulo cuando sus extremos se toquen.
 Por ejemplo, si todas las varillas tienen una longitud de 6 centímetros.
 Entonces uno puede construir fácilmente un triángulo equilátero con ellos.
 Sin embargo, si una varillas es de 6 centímetros de largo,
 mientras que los otros dos son cada uno de solo 2 centímetros de largo,
 entonces no se puede formar un triángulo. En general, si una longitud es mayor o igual que
 la suma de las otras dos, entonces las longitudes no pueden usarse para formar un triángulo.
 De lo contrario, pueden formar un triángulo. Escriba una función que determine
 si tres longitudes pueden formar un triángulo.
 La función tomará 3 parámetros y devolverá un resultado booleano. Además,
 escriba un programa que lea 3 longitudes del usuario
 y muestre el comportamiento de esta función.
'''

def determinar(varilla1, varilla2, varilla3):
    if varilla1 >= (varilla2 + varilla3):
        return False
    elif varilla2 >= (varilla1 + varilla3):
        return False
    elif varilla3 >= (varilla2 + varilla1):
        return False
    else:
        return True

def leer_longitudes():
    longitud1 = float(input("Ingrese la primer longitud: "))
    longitud2 = float(input("Ingrese la segunda longitud: "))
    longitud3 = float(input("Ingrese la tercer longitud: "))
    if determinar(longitud1, longitud2, longitud3):
        print("Se puede formar un triangulo con las longitudes ingresadas.")
    else:
        print("No se puede formar un triangulo con las longitudes dadas.")

leer_longitudes()