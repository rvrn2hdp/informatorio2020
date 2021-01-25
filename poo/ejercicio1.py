class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad} Km/h\nCilindrada: {self.cilindrada}cc"

micoche = Coche("rojo", 4, 0, 130)
print(type(micoche).__name__)
print(micoche)