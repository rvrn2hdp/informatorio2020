''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Escribir un programa que pregunte el nombre del usuario en la consola 
    y después de que el usuario lo introduzca muestre por pantalla 
    <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
    mayúsculas y <n> es el número de letras que tienen el nombre.
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea

nombre = input("Ingrese su nombre: ")
print(nombre.upper(), "tiene", len(nombre), "letras")


'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Escribir un programa que pida al usuario dos números, que luego 
    calcule y muestre por pantalla su división. 
    Si el divisor es cero el programa debe mostrar un error e imprimir 
    por pantalla el resultado e indicar si es par o impar.
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea

n1 = int(input("\nIngrese un número: "))
n2 = int(input("Ingrese un número: "))
if n2 == 0:
    print("ERROR: no se puede dividir por 0.")
else:
    resultado = n1/n2
    if resultado % 2 == 0:
        print(resultado, "es par.")
    else:
        print(resultado, "es impar.")
        
'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Escribir un programa que pida al usuario un número entero 
    y muestre por pantalla un triángulo rectángulo como el de más abajo, 
    de altura el número introducido.

    *
    **
    ***
    ****
    *****
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea

num1 = int(input("Ingrese un número: "))
cont = 0
while cont < num1:
    cont += 1
    print('*' * cont)


'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Dados los datos de un municipio: zona, sexo y edad de cada uno de 
    sus habitantes, encontrar:
    a) porcentaje de varones menores de 15 años para cada zona
    b) porcentaje de varones menores de 15 años para todo el municipio
    A su vez debera imprimir además del porcentaje mencionado arriba, 
    la cantidad de varones menores de 15 años total de toda la zona y del municipio.
    Los datos vienen ordenados por zona. Con dato de zona igual a 0, se indica el fin.
'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea

print("Programa que determina el porcentaje de varones menores que hay en zonas de un minicipio:")

def verificar_edad():
    sexo = int(input("\nSexo:\n1 - Femenino\n2 - Masculino\nIngrese una opcion: "))
    edad = int(input("\nIngrese su edad: "))
    if sexo == 2 and edad < 15:
        return True
    else:
        return False

zona = 1
personas = 0
zona_norte = 0
zona_sur = 0
zona_este = 0
zona_oeste = 0
menores = 0

while zona != 0:
    zona = int(input("\nZonas:\n1 - Norte\n2 - Sur\n3 - Este\n"
                     "4 - Oeste\n0 - Salir\nIngrese una opcion: "))
    if zona == 0:
        break
    elif zona == 1:
        if verificar_edad() == True:
            zona_norte += 1
            menores += 1
    elif zona == 2:
        if verificar_edad() == True:
            zona_sur += 1
            menores += 1
    elif zona == 3:
        if verificar_edad() == True:
            zona_este += 1
            menores += 1
    elif zona == 4:
        if verificar_edad() == True:
            zona_norte += 1
            menores += 1
    else:
        print("dato ingresado incorrecto.")
        continue
        
    personas += 1

print(f"Hay", zona_norte, " varones menores de 15 años en la zona Norte del municipio,"
      " el porcentaje es %", ((zona_norte//personas)*100))
print("Hay", zona_sur, " varones menores de 15 años en la zona Sur del municipio,"
      " el porcentaje es %", ((zona_sur//personas)*100))
print("Hay", zona_este, " varones menores de 15 años en la zona Este del municipio,"
      " el porcentaje es %", ((zona_este//personas)*100))
print("Hay", zona_oeste, " varones menores de 15 años en la zona Oeste del municipio,"
      " el porcentaje es %", ((zona_oeste//personas)*100))
print("Hay", menores, " varones menores de 15 años en el municipio,"
      " el porcentaje es %", ((menores//personas)*100))
