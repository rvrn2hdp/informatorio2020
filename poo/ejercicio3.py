'''ejercicio 3
 Desarrollar un programa que cargue los datos de un triángulo.
 Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del
 lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).
'''

class Triangulo:
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0
    
    def inicializar(self):
        self.lado1 = float(input("Ingrese el valor del primer lado: "))
        self.lado2 = float(input("Ingrese el valor del segundo lado: "))
        self.lado3 = float(input("Ingrese el valor del tercer lado: "))
 
    def imprimir(self):
        print("Los lados del triángulo tienen el valor de:")
        print("Lado 1:", self.lado1)
        print("Lado 2:", self.lado2)
        print("Lado 3:", self.lado3)
        
    def mayor(self):
        print("El lado mayor es")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("Lado 1:", self.lado1)
        elif self.lado2 > self.lado3:
            print("Lado 2:", self.lado2)
        else:
            print("Lado 3:", self.lado3)
 
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triángulo equilátero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")

figura=Triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()