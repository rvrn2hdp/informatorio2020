'''Ejercicio 3: Calculadora de envío
 Un minorista en línea proporciona una forma de envío urgente de $ 10.95
 para el primer elemento y $ 2.95 para cada segundo elemento posterior. 
 Escriba una función que tome el número de elementos en el pedido como su único parámetro. 
 Devuelva los gastos de envío del pedido como resultado de la función. Incluya un programa principal
 que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío.'''



def calcular_precio(elementos):
    total = 10.95
    while elementos > 1:
        total += 2.95
        elementos -= 1
    
    return total

def main():
    print("\nprograma que calcula los precios de envio de elementos\n")
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    print("El precio total del envio es: $", round(calcular_precio(cantidad)))
    
main()