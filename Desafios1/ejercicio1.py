# se guardan la cantidad de preguntas y respuestas correctas.

preguntas = int(input("Ingrese la cantidad de preguntas del cuestionario: "))
respuestas = int(input("Ingrese la cantidad de respuestas correctas del cuestionario: "))

# se calcula el porcentaje de respuestas correctas.

resultado = (respuestas / preguntas) * 100

# se crea una variable que guardará el string con el resultado final del cuestionario.

final = None

# se compara el porcentaje de respuestas correctas con el porcentaje de cada nota final.

if resultado >= 90:
    final = "EXELENTE"
elif resultado >= 70:
    final = "BUENO"
elif resultado >= 60:
    final = "APROBADO"
elif resultado < 60:
    final = "NO APROBADO"

# se muestra a que resultado final pertenece la cantidad de respuestas correctas del cuestionario.

print("el resultado final es", final)
