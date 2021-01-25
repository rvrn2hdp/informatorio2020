"""Se está desarrollando un sistema de control de vehículos
 desde donde se han tirado restos de basura a la vía pública.
 Para ello la ciudad cuenta con sistemas de monitoreo de patentes
 que devuelve 3 letras y un valor numérico de 5 dígitos a la Central
 con el siguiente significado:
    3 letras: Correspondientes a la patente.
    Del valor numérico:
        Los 3 primeros números corresponden a la patente
        El 4 número indica
            1 - Tiró basura a la vía pública 
            0 - No tiró basura a la vía pública
        El 5 número indica
            1 - Ya había sido multado el vehículo
            0 - Vehículo sin multas.
 Deberás informar cantidad de vehículos observados, cantidad de vehículos
 que han tirado basura y porcentaje de éstos que ya habían sido multados.
"""

print("\nBienvenido\n")
tiro_basura = 0
ya_multado = 0
analizadas = 0

while True:
    patente = input("\nIngrese la patente: ")
    analizadas += 1
    if patente [6] == '1':
        tiro_basura += 1

    if patente [7] == '1':
        ya_multado += 1
    
    seguir = int(input("\n1 - Siguiente patente\n2 - Terminar de analizar patentes\n"))
    if seguir == 2:
        break
    
print("\nSe analizaron", analizadas, "patentes")
print(tiro_basura, "tiraron basura")
print("y", ya_multado, "ya habían sido multados.\n")