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

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad} Km/h\nCilindrada: {self.cilindrada}cc\nCarga: {self.carga}Kg"
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}\nVelocidad: {self.velocidad}Km/h\nCilindrada: {self.cilindrada}cc"

miCamioneta = Camioneta("Gris", 4, 80, 100, 1000)
miMotocicleta = Motocicleta("Rojo", 2, "Deportivo", 150, 130)
miBicicleta = Bicicleta("Negro", 2, "Deportivo")

misVehiculos = [miCamioneta, miMotocicleta, miBicicleta]

def catalogar(vehiculos, ruedas = None):
    cantidad = 0
    
    for vehiculo in vehiculos:
        print(type(vehiculo).__name__)
        print(vehiculo, "\n")
        if ruedas == vehiculo.ruedas:
            cantidad +=1
    
    if ruedas != None:
        print(f"Se han encontrado {cantidad} vehículos con {ruedas} ruedas.")
    
catalogar(misVehiculos, 0)
