""".La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes
para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y Rúcula .
Ingredientes no vegetarianos: Jamón y Panceta.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un
ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva"""

pizza_veget = ["Pimiento", "Rúcula"]
pizza_no_veget = ["Jamón", "Panceta"]

print("  Bienvenidos a Bella Napoli")
print("¿Quiere una pizza vegetariana?")
opc = str(input("Si/No: "))

ingredientes = []
tipo_de_pizza = None

if opc == 'Si' or opc == 'si':
    ingredientes = pizza_veget
    tipo_de_pizza = 'vegetariana'

elif opc == 'No' or opc == 'no':
    ingredientes = pizza_no_veget
    tipo_de_pizza = 'no vegetariana'

cont = 0
print("\n¿Qué ingrediente quiere?")
for i in ingredientes:
    cont += 1
    print(cont, "-", i)

opc = int(input("Elija una opción: "))

cont = 0
pizza = []
for j in ingredientes:
    cont += 1
    if cont == opc:
        pizza = j + " Mozzarella" + " Tomate"
        break

print("\nSu pizza será", tipo_de_pizza, "y tendrá estos ingredientes:")
print(pizza, sep='\n')