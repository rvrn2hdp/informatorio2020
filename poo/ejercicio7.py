"""En un depósito se guardan las bebidas a comercializar.
 Estos productos son bebidas como agua mineral y gaseosas. 
 De los productos nos interesa saber su
 identificador (cada uno tiene uno distinto), cantidad de litros, precio y marca.
 Si es agua mineral nos interesa saber también el origen (Manantial, Ciudad, etc).
 Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y
 si tiene o no alguna promoción (si la tiene tendrá un descuento del 10% en el precio).
 Las operaciones del almacén son las siguientes:
  Calcular precio de todas las bebidas: calcula el precio total de todos los productos del almacén.
  Calcular el precio total de una marca de bebida: dada una marca, calcular el precio total de esas bebidas.
  Agregar producto: agrega un producto, si el identificador esta
                    repetido en alguno de las bebidas, no se agregará esa bebida.
  Eliminar un producto: dado un ID, eliminar el producto del depósito.
  Mostrar información: mostramos para cada bebida toda su información.
"""

class Almacen():
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, nproducto):
        if len(self.productos) == 0:
            self.productos.append(nproducto)
        else:
            for producto in self.productos:
                if producto.identificador == nproducto.identificador:
                    print("No se puede agregar este producto: ID ya agregado.")
                else:
                    self.productos.append(nproducto)
    
    def eliminar_producto(self, identificador):
        if len(self.productos) == 0:
            print("No hay Productos en el almacen.")
        else:
            for producto in self.productos:
                if producto.identificador == identificador:
                    eliminado = self.productos.pop(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(type(producto).__name__)
            print(producto)

    def total_todo(self):
        total = 0.0
        for producto in self.productos:
            total += producto.precio
        print(f"El total de todas las bebidas es: {total}")
    
    def total_marca(self, marca):
        total = 0.0
        for producto in self.productos:
            if producto.marca == marca:
                total += producto.precio
        print(f"El total de los productos de {marca} es: {total}")

class Producto():
    def __init__(self, identificador, litros, precio, marca):
        self.identificador = identificador
        self.litros = litros
        self.precio = precio
        self.marca = marca
    
    def __str__(self):
        return f"""Identificador: {self.identificador}\nLitros: {self.litros}\n
            Precio: ${self.precio}\nMarca: {self.marca}"""
    
class AguaMineral(Producto):
    # origen: Manantial, Ciudad, etc...
    def __init__(self, identificador, litros, precio, marca, origen):
        super().__init__(identificador, litros, precio, marca)
        self.origen = origen
    
    def __str__(self):
        return f"""Identificador: {self.identificador}\nLitros: {self.litros}\n
            Precio: ${self.precio}\nMarca: {self.marca}\nOrigen: {self.origen}"""

class Gaseosa(Producto):
    def __init__(self, identificador, litros, precio, marca, azucar, promocion):
        super().__init__(identificador, litros, precio, marca)
        self.azucar = azucar
        self.promocion = promocion

    def __str__(self):
        return f"""Identificador: {self.identificador}\nLitros: {self.litros}\n
            Precio: ${self.precio}\nMarca: {self.marca}\n
            Azucar: {self.azucar}\nPromoción: {self.promocion}"""