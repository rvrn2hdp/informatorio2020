"""
En una tienda de descuento por reciclado las personas que van a pagar
  el importe de su compra llegan a la caja y ofrecen tapitas para reciclar,
  de acuerdo a la cantidad que lleven en la caja le entregan un código de
  descuento que se aplicará sobre el total de su compra. Determinar la cantidad
  que pagara cada cliente desde que la tienda abre hasta que cierra. 
Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento;
  si es amarilla un 25% y si es blanca no obtendrá descuento.
"""

print("\nprograma que simula el funcionamiento de una caja con descuentos...")

def menu_de_colores():
    print("""
    \nSeleccione el color del ticket de descuento:
    \n1 - Rojo
    \n2 - Amarillo
    \n3 - Blanco
    """)

while True:
    total = float(input("Ingrese el total de la compra del cliente: "))
    menu_de_colores()
    opc = int(input())
    if opc == 1:
        print("\nEl total de su compra será: $", (total - total * 0.4))
    elif opc == 2:
        print("\nEl total de su compra será: $", (total - total * 0.25))
    elif opc == 3:
        print("\nEl total de su compra será: $", total)
    else:
        print("opción ingresada incorrecta.")
        print("Ingrese nuevamente el monto y el color:")
        continue

    if int(input("desea cerrar la caja?\n1 - SI\n2 - NO\n")) == 1:
        break


