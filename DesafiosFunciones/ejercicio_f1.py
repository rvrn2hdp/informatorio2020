'''Desafío 1
 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y
 una botella de PET puede tardar 1.000 años en desaparecer. 
 Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
 Un trozo de chicle tarda 5 años en degradarse. 
 Se solicita una función para que dado el ingreso de un elemento,
 se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle,
 e imprima la cantidad de años que tarda en degradarse.
'''

def degradacion(elemento):
    if elemento == 1:
        print("Tarda 150 años en degradarse.")
    elif elemento == 2:
        print("Tarda 1.000 años en desaparecer.")
    elif elemento == 3:
        print("Tarda hasta 30 años en degradarse.")
    elif elemento == 4:
        print("Tarda 5 años en degradarse.")
    else:
        print("Opcion incorrecta.")

def menu():
    print("\nElementos a seleccionar:")
    print("1 - Bolsa de plastico")
    print("2 - Botella de PET")
    print("3 - Envases de tetrabrik")
    print("4 - Chicle")

    argumento = int(input("ingrese un número: "))
    return argumento

degradacion(menu())