"""Estudiantes de un curso se han dividido en dos grupos A y B de acuerdo al turno y el
nombre. El grupo A está formado por estudiantes del turno Tarde con un nombre anterior
a la M y estudiantes del turno Noche con un nombre posterior a la N y el grupo B por el
resto. Escribir un programa que pregunte al usuario su nombre y turno, y muestre por
pantalla el grupo que le corresponde."""

nombre = input("Ingrese su nombre: ")
turno = input("Ingrese el turno al que pertenece (Tarde/Noche): ")

if turno == "Tarde":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("El grupo al que pertenece es:", grupo)
