'''
 Escriba una función que tome las longitudes de los dos lados más cortos
 de un triángulo rectángulo como sus parámetros y devuelva la hipotenusa del triángulo,
 calculada usando el teorema de Pitágoras, como resultado de la función. 
 Incluya un programa principal que lea las longitudes
 de los lados más cortos de un triángulo rectángulo del usuario,
 use su función para calcular la longitud de la hipotenusa y muestre el resultado.
'''

def hipotenusa(lado1, lado2):
    return lado1**2 + lado2**2

def main():
    print("\nInicio de Programa\n")
    print("programa que calcula la hipotenusa de un triangulo\n")
    num1 = float(input("Ingrese el primer lado: "))
    num2 = float(input("Ingrese el segundo lado: "))
    print("\nla hipotenusa del triangulo es:", hipotenusa(num1, num2))
    print("\nFin de programa")

main()