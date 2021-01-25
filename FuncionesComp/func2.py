'''Ejercicio 2: Tarifa del taxi
 En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00,
 más $15.00 por cada 140 metros recorridos. Escriba una función que tome la distancia
 recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado.
 Escriba un programa principal que use la función.
 Sugerencia: Utilice constantes para presentar la base y la porción variable
 de las tarifas así el programa podrá actualizar fácilmente cuando las tasas aumentan.
 '''

def tarifa(km):
    tarifa = 40.00
    metro = km * 1000
    
    while metro > 140:
        tarifa += 15.00
        metro -= 140
    
    return tarifa

def programa_principal():
    print("\nPrograma que calcula la tarifa de taxi según los kilometros recorridos:\n")
    kilometros = float(input("Ingrese la distancia recorrida (Km): "))
    print("\nLa tarifa sería:", tarifa(kilometros))

programa_principal()