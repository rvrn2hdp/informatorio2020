""" Intenta desarrollar un programa que solicite que te
ingresen las ventas de 2 días. Y luego se informe por
pantalla si se vendió más el día 1, el día 2, o si se
vendió lo mismo en ambos días. """

dia1 = float(input("ingrese las ventas del primer dia:"))
dia2 = float(input("ingrese las ventas del segundo dia:"))

if dia1>dia2:
    print("se vendió mas el primer día.")
elif dia1<dia2:
    print("se vendió mas el segundo día.")
elif dia1==dia2:
    print("se vendió lo mismo en ambos días.")
