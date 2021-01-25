def mostrar_menu():
    print("\n\t¿Qué tamaño tiene el pez?")
    print("1 - Tamaño normal")
    print("2 - Tamaño por debajo de lo normal")
    print("3 - Tamaño un poco por encima de lo normal")
    print("4 - Tamaño sobredimensionado")

def leer_opcion():
    opc = int(input())
    return opc

def estado_de_pez(opcion):
    if opcion == 1:
        print("Pez en buenas condiciones.")
    elif opcion == 2:
        print("Pez con problemas de nutrición.")
    elif opcion == 3:
        print("Pez con sintomas de organismo contaminado.")
    elif opcion == 4:
        print("Pez contaminado.")
    else:
        print("dato incorrecto")
    
    print("\n")

mostrar_menu()
estado_de_pez(leer_opcion())
